import logging
import pandas as pd
import os
import numpy as np
import re
import pickle
import json
from collections import OrderedDict, defaultdict
from torch.utils.data import Dataset
from sklearn.preprocessing import MinMaxScaler
from tikuna.common.utils import decision


def load_sessions(data_dir):
    with open(os.path.join(data_dir, "data_desc.json"), "r") as fr:
        data_desc = json.load(fr)
    with open(os.path.join(data_dir, "session_train.pkl"), "rb") as fr:
        session_train = pickle.load(fr)
    with open(os.path.join(data_dir, "session_test.pkl"), "rb") as fr:
        session_test = pickle.load(fr)

    train_labels = [
        v["label"] if not isinstance(v["label"], list) else int(sum(v["label"]) > 0)
        for _, v in session_train.items()
    ]
    test_labels = [
        v["label"] if not isinstance(v["label"], list) else int(sum(v["label"]) > 0)
        for _, v in session_test.items()
    ]

    num_train = len(session_train)
    ratio_train = sum(train_labels) / num_train
    num_test = len(session_test)
    ratio_test = sum(test_labels) / num_test
    logging.info("Load from {}".format(data_dir))
    logging.info(json.dumps(data_desc, indent=4))
    logging.info(
        "# train sessions {} ({:.2f} anomalies)".format(num_train, ratio_train)
    )
    logging.info("# test sessions {} ({:.2f} anomalies)".format(num_test, ratio_test))
    return session_train, session_test

class log_dataset_scores(Dataset):
    def __init__(self, scores):
        peers = scores.peer.unique()
        score_values = scores.iloc[:,-3:]

        # apply normalization techniques
        score_values_tensor = score_values.to_numpy()

        # Normalise features
        sc = MinMaxScaler(feature_range = (0, 1))
        score_values_tensor = sc.fit_transform(score_values_tensor)
        score_values_tensor = pd.DataFrame(score_values_tensor)
        score_values_tensor["peer"] = scores["peer"].reset_index(drop=True)
        score_values_tensor["honest"] = scores["honest"].reset_index(drop=True)

        # Create slidding windows
        steps = 10

        # Prepare the training data
        flatten_data_list = []

        for peer in peers:
            peer_values = score_values_tensor.loc[score_values_tensor["peer"] == peer]
            honest = 0 if True in peer_values.honest.unique() else 1
            peer_values = peer_values.iloc[: , :3]
            for i in range(steps, peer_values.shape[0]-steps):
                features = peer_values.iloc[i-steps:i, :].values
                labels = peer_values.iloc[i, :].values
                sample = {
                    "session_idx": peer,
                    "features": features,
                    "window_labels": labels,
                    "window_anomalies": honest,
                }
                flatten_data_list.append(sample)
        self.flatten_data_list = flatten_data_list

    def __len__(self):
        return len(self.flatten_data_list)

    def __getitem__(self, idx):
        return self.flatten_data_list[idx]

class log_dataset_traces(Dataset):
    def __init__(self, traces):
        peers = traces.peer.unique()
        # Eclipse single
        trace_values = traces.iloc[:,0:5]
        # Covert
        # trace_values = traces.iloc[:,1:11]
        # Eclipse network
        # trace_values = traces.iloc[:,0:8]

        # apply normalization techniques
        trace_values_tensor = trace_values.to_numpy()

        # Normalise features
        sc = MinMaxScaler(feature_range = (0, 1))
        trace_values_tensor = sc.fit_transform(trace_values_tensor)
        trace_values_tensor = pd.DataFrame(trace_values_tensor)
        trace_values_tensor["peer"] = traces["peer"].reset_index(drop=True)
        trace_values_tensor["honest"] = traces["honest"].reset_index(drop=True)

        # Create slidding windows
        steps = 6

        # Prepare the training data
        flatten_data_list = []

        for peer in peers:
            peer_values = trace_values_tensor.loc[trace_values_tensor["peer"] == peer]
            honest = 0 if True in peer_values.honest.unique() else 1
            peer_values = peer_values.iloc[: , :5]
            for i in range(steps, peer_values.shape[0]-steps):
                features = peer_values.iloc[i-steps:i, :].values
                labels = peer_values.iloc[i, :].values
                sample = {
                    "session_idx": peer,
                    "features": features,
                    "window_labels": labels,
                    "window_anomalies": honest,
                }
                flatten_data_list.append(sample)
        self.flatten_data_list = flatten_data_list

    def __len__(self):
        return len(self.flatten_data_list)

    def __getitem__(self, idx):
        return self.flatten_data_list[idx]

class log_dataset_octets(Dataset):
    def __init__(self, logs, labels):
        # Extract tensor
        log_values_tensor = logs.to_numpy()
        # apply normalization techniques
        sc = MinMaxScaler(feature_range = (0, 1))
        log_values_tensor = sc.fit_transform(logs)
        log_values_tensor = pd.DataFrame(log_values_tensor)

        # Create slidding windows
        steps = 10

        # Prepare the training data
        flatten_data_list = []

        for i in range(steps, log_values_tensor.shape[0]-steps):
            features = log_values_tensor.iloc[i-steps:i, :].values
            next_log = log_values_tensor.iloc[i, :].values
            window_anomaly = 0
            # If one of the data is anomaluous all the data is anomalous
            if labels is not None and labels.iloc[i-steps:i, :].sum().item() > 0:
                window_anomaly = 1
            sample = {
                "session_idx": 0,
                "features": features,
                "window_labels": next_log,
                "window_anomalies": window_anomaly,
            }
            flatten_data_list.append(sample)
        self.flatten_data_list = flatten_data_list

    def __len__(self):
        return len(self.flatten_data_list)

    def __getitem__(self, idx):
        return self.flatten_data_list[idx]

class log_dataset(Dataset):
    def __init__(self, session_dict, feature_type="semantics"):
        flatten_data_list = []
        # flatten all sessions
        for session_idx, data_dict in enumerate(session_dict.values()):
            features = data_dict["features"][feature_type]
            window_labels = data_dict["window_labels"]
            window_anomalies = data_dict["window_anomalies"]
            for window_idx in range(len(window_labels)):
                sample = {
                    "session_idx": session_idx,  # not session id
                    "features": features[window_idx],
                    "window_labels": window_labels[window_idx],
                    "window_anomalies": window_anomalies[window_idx],
                }
                flatten_data_list.append(sample)
        self.flatten_data_list = flatten_data_list

    def __len__(self):
        return len(self.flatten_data_list)

    def __getitem__(self, idx):
        return self.flatten_data_list[idx]
