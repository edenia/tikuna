import os
import io
import itertools
import torch
import numpy as np
from collections import Counter, defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.base import BaseEstimator
import hashlib
import pickle
import re
import logging
from tqdm import tqdm

from tikuna.common.utils import (
    json_pretty_dump,
    dump_pickle,
    load_pickle,
)


def load_vectors(fname):
    logging.info("Loading vectors from {}.".format(fname))
    if fname.endswith("pkl"):
        with open(fname, "rb") as fr:
            data = pickle.load(fr)
    else:
        fin = io.open(fname, "r", encoding="utf-8", newline="\n", errors="ignore")
        n, d = map(int, fin.readline().split())
        data = {}
        for line in fin.readlines()[0:1000]:
            tokens = line.rstrip().split(" ")
            data[tokens[0]] = np.array(list(map(float, tokens[1:])))
    return data


class Vocab:
    def __init__(self, max_token_len, min_token_count, use_tfidf=False):
        self.max_token_len = max_token_len
        self.min_token_count = min_token_count
        self.use_tfidf = use_tfidf
        self.word2idx = {"PADDING": 0, "OOV": 1}
        self.token_vocab_size = None

    def __tokenize_log(self, log):
        word_lst = []
        word_lst.append(log.lower())
        return word_lst

    def gen_pretrain_matrix(self, pretrain_path):
        logging.info("Generating a pretrain matrix.")
        word_vec_dict = load_vectors(pretrain_path)
        vocab_size = len(self.word2idx)
        pretrain_matrix = np.zeros([vocab_size, 300])
        oov_count = 0

        for word, idx in tqdm(self.word2idx.items()):
            if word in word_vec_dict:
                pretrain_matrix[idx] = word_vec_dict[word]
            else:
                oov_count += 1
        logging.info(
            "{}/{} words are assgined pretrained vectors.".format(
                vocab_size - oov_count, vocab_size
            )
        )
        return torch.from_numpy(pretrain_matrix)

    def trp(self, l, n):
        """ Truncate or pad a list """
        r = l[:n]
        if len(r) < n:
            r.extend(list([0]) * (n - len(r)))
        return r

    def build_vocab(self, logs):
        token_counter = Counter()
        for log in logs:
            tokens = self.__tokenize_log(log)
            token_counter.update(tokens)
        valid_tokens = set(
            [
                word
                for word, count in token_counter.items()
                if count >= self.min_token_count
            ]
        )
        self.word2idx.update({word: idx for idx, word in enumerate(valid_tokens, 2)})
        self.token_vocab_size = len(self.word2idx)

    def fit_tfidf(self, total_logs):
        logging.info("Fitting tfidf.")
        total_logs = [str (item) for item in total_logs]
        self.tfidf = TfidfVectorizer(
            tokenizer=lambda x: self.__tokenize_log(x),
            vocabulary=self.word2idx,
            norm="l1",
        )
        self.tfidf.fit(total_logs)

    def transform_tfidf(self, logs):
        logs = set(map(str, logs))
        return self.tfidf.transform(logs)

    def logs2idx(self, logs):
        idx_list = []
        for log in logs:
            tokens = self.__tokenize_log(str(log))
            tokens_idx = self.trp(
                [self.word2idx.get(t, 1) for t in tokens], self.max_token_len
            )
            idx_list.append(tokens_idx)
        return idx_list


class FeatureExtractor(BaseEstimator):
    """
    feature_type: "sequentials", "semantics", "quantitatives"
    window_type: "session", "sliding"
    max_token_len: only used for semantics features
    """

    def __init__(
        self,
        label_type="next_log",
        feature_type="sequentials",
        eval_type="session",
        window_type="sliding",
        window_size=None,
        stride=None,
        max_token_len=50,
        min_token_count=1,
        pretrain_path=None,
        use_tfidf=False,
        cache=False,
        evaluation=False,
        **kwargs,
    ):
        self.label_type = label_type
        self.feature_type = feature_type
        self.eval_type = eval_type
        self.window_type = window_type
        self.window_size = window_size
        self.stride = stride
        self.pretrain_path = pretrain_path
        self.use_tfidf = use_tfidf
        self.max_token_len = max_token_len
        self.min_token_count = min_token_count
        self.cache = cache
        self.vocab = Vocab(max_token_len, min_token_count)
        self.meta_data = {}
        self.evaluation = evaluation
        self.model_loaded = False

        if cache and not evaluation:
            param_json = self.get_params()
            identifier = hashlib.md5(str(param_json).encode("utf-8")).hexdigest()[0:8]
            self.cache_dir = os.path.join("/home/tikuna/app/data/tikuna_model_data", identifier)
            os.makedirs(self.cache_dir, exist_ok=True)
            json_pretty_dump(
                param_json, os.path.join(self.cache_dir, "feature_extractor.json")
            )
        else:
            self.cache_dir = os.path.join("/home/tikuna/app/data/tikuna_model_data", "production")

    def __generate_windows(self, data, stride):
        session_dict = {}
        window_count = 0
        row_size = data["features"].shape[1]
        data_list = list(itertools.chain(*[row for index, row in data["features"].iterrows()]))
        for i in range(self.window_size, len(data_list)-self.window_size):
            windows = []
            window_labels = []
            window_anomalies = []
            window = data_list[i-self.window_size:i]
            next_log = self.log2id_train.get(data_list[i], 1)
            window_anomaly = 0

            # If one of the data is anomaluous all the data is anomalous
            # new data does not have a label
            if "label" in data \
            and data["label"].iloc[(int)((i-self.window_size)/row_size):(int)(i/row_size)].sum().item() > 0:
                window_anomaly = 1

            windows.append(window)
            window_labels.append(next_log)
            window_anomalies.append(window_anomaly)
            window_count += 1

            session_dict[window_count] = {}
            session_dict[window_count]["windows"] = windows
            session_dict[window_count]["window_labels"] = window_labels
            session_dict[window_count]["window_anomalies"] = window_anomalies

        logging.info("{} sliding windows generated.".format(window_count))
        return session_dict

    def __windows2quantitative(self, windows):
        total_features = []
        for window in windows:
            feature = [0] * len(self.id2log_train)
            window = [self.log2id_train.get(x, 1) for x in window]
            log_counter = Counter(window)
            for logid, log_count in log_counter.items():
                feature[int(logid)] = log_count
            total_features.append(feature[1:])  # discard the position of padding
        return np.array(total_features)

    def __windows2sequential(self, windows):
        total_features = []
        for window in windows:
            ids = [self.log2id_train.get(x, 1) for x in window]
            total_features.append(ids)
        return np.array(total_features)

    def __window2semantics(self, windows, log2idx):
        # input: raw windows
        # output: encoded token matrix,
        total_idx = [list(map(lambda x: log2idx[x], window)) for window in windows]
        return np.array(total_idx)

    def save(self):
        logging.info("Saving feature extractor to {}.".format(self.cache_dir))
        with open(os.path.join(self.cache_dir, "est.pkl"), "wb") as fw:
            pickle.dump(self, fw)

    def load(self):
        try:
            if self.model_loaded:
                return True
            if self.evaluation:
                self.cache_dir = os.path.join("/home/tikuna/app/data/tikuna_model_data", "production")
                self.model_loaded = True
            save_file = os.path.join(self.cache_dir, "est.pkl")
            logging.info("Loading feature extractor from {}.".format(save_file))
            with open(save_file, "rb") as fw:
                obj = pickle.load(fw)
                self.__dict__ = obj.__dict__
                return True
        except Exception as e:
            logging.info("Cannot load cached feature extractor.")
            return False

    def fit(self, data, datatype="train"):
        if self.load():
            return
        log_padding = "<pad>"
        log_oov = "<oov>"
        self.vocab_size_test = 0

        # encode
        total_logs = list(
            itertools.chain(*[row for index, row in data["features"].iterrows()])
        )

        if datatype == "train":
            self.complete_logs = total_logs
            self.ulog_train = set(total_logs)
            self.id2log_train = {0: log_padding, 1: log_oov}
            self.id2log_train.update(
                {idx: log for idx, log in enumerate(self.ulog_train, 2)}
            )
            self.log2id_train = {v: k for k, v in self.id2log_train.items()}
            self.vocab_size_train = len(self.log2id_train)
            logging.info("{} words are found in training data.".format(self.vocab_size_train))
        else:
            self.complete_logs.extend(total_logs)
            self.ulog_test = set(total_logs)
            self.ulog_train.update(set(total_logs))
            training_size = len(self.id2log_train)
            self.id2log_train.update(
                {idx: log for idx, log in enumerate(self.ulog_test, training_size)}
            )
            self.log2id_train.update({v: k for k, v in self.id2log_train.items()})
            self.vocab_size_test = len(self.log2id_train)
            logging.info("{} words are found in testing data.".format(self.vocab_size_test))

        if self.label_type == "next_log":
            self.meta_data["num_labels"] = self.vocab_size_train + self.vocab_size_test
        elif self.label_type == "anomaly":
            self.meta_data["num_labels"] = 2
        else:
            logging.info('Unrecognized label type "{}"'.format(self.label_type))
            exit()

        if self.feature_type == "semantics":
            logging.info("Using semantics.")
            logging.info("Building vocab.")
            self.vocab.word2idx = self.log2id_train
            self.vocab.token_vocab_size = len(self.vocab.word2idx)
            logging.info("Building vocab done.")
            self.meta_data["vocab_size"] = self.vocab_size_train + self.vocab_size_test

            if self.pretrain_path is not None:
                logging.info(
                    "Using pretrain word embeddings from {}".format(self.pretrain_path)
                )
                self.meta_data["pretrain_matrix"] = self.vocab.gen_pretrain_matrix(
                    self.pretrain_path
                )
            if self.use_tfidf:
                self.vocab.fit_tfidf(total_logs)

        elif self.feature_type == "sequentials":
            self.meta_data["vocab_size"] = self.vocab_size_train + self.vocab_size_test

        else:
            logging.info('Unrecognized feature type "{}"'.format(self.feature_type))
            exit()

        if self.cache:
            self.save()

    def transform(self, data, datatype="train"):
        session_dict = {}
        logging.info("Transforming {} data.".format(datatype))
        ulog = set(itertools.chain(*[row for index, row in data["features"].iterrows()]))
        if datatype == "test":
            # handle new logs
            ulog_new = ulog - self.ulog_train

        if self.evaluation:
            self.cache_dir = os.path.join("/home/tikuna/app/data/tikuna_model_data", "production")

        if self.cache:
            cached_file = os.path.join(self.cache_dir, datatype + ".pkl")
            if os.path.isfile(cached_file):
                return load_pickle(cached_file)

        session_dict = self.__generate_windows(data, self.stride)

        if self.feature_type == "semantics":
            if self.use_tfidf:
                indice = self.vocab.transform_tfidf(self.complete_logs).toarray()
            else:
                indice = np.array(self.vocab.logs2idx(self.complete_logs))
            log2idx = {log: indice[idx] for idx, log in enumerate(self.complete_logs)}
            log2idx["PADDING"] = np.zeros(indice.shape[1]).reshape(-1)
            logging.info("Extracting semantic features.")

        for session_id, data_dict in session_dict.items():
            feature_dict = defaultdict(list)
            windows = data_dict["windows"]
            # generate sequential feautres # sliding windows on logid list
            if self.feature_type == "sequentials":
                feature_dict["sequentials"] = self.__windows2sequential(windows)

            # generate semantics feautres # use logid -> token id list
            if self.feature_type == "semantics":
                feature_dict["semantics"] = self.__window2semantics(windows, log2idx)

            # generate quantitative feautres # count logid in each window
            if self.feature_type == "quantitatives":
                feature_dict["quantitatives"] = self.__windows2quantitative(windows)

            session_dict[session_id]["features"] = feature_dict

        logging.info("Finish feature extraction ({}).".format(datatype))
        if self.cache:
            dump_pickle(session_dict, cached_file)
        return session_dict

    def fit_transform(self, session_dict, datatype="train"):
        self.fit(session_dict, datatype)
        return self.transform(session_dict, datatype)
