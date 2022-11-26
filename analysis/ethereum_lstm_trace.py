NORMAL_DATA_DIR="./normal"
ECLIPSE_PUBLISHERS_DATA_DIR="./eclipse-publishers"
ECLIPSE_SINGLE_DATA_DIR="./eclipse-single-trace"
ECLIPSE_NET="./eclipse-net"
DERIVE_MESHES=False
MESH_SAMPLE_FREQ='5s'

import sys
sys.path.append("../")
import argparse
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import toml
import ipywidgets as widgets
import json
import pathlib
import seaborn as sns
import notebook_helper

from pprint import pprint
from durations import Duration

from notebook_helper import no_scores_message, load_pandas, archive_figures, load_trace_data
from notebook_helper import p25, p50, p75, p95, p99, b64_to_b58, numeric_peer_id
from torch.utils.data import DataLoader
from sklearn.preprocessing import MinMaxScaler
from tikuna.models import LSTM
from tikuna.common.preprocess import FeatureExtractor
from tikuna.common.dataloader import load_sessions, log_dataset, log_dataset_scores, log_dataset_traces
from tikuna.common.utils import seed_everything, dump_final_results, dump_params

traces = load_trace_data(NORMAL_DATA_DIR)
traces_anomaly = load_trace_data(ECLIPSE_NET)
traces_anomaly["honest"] = ~traces_anomaly["honest"]
print(traces_anomaly.shape)
print(traces_anomaly.to_string())

parser = argparse.ArgumentParser()

##### Model params
parser.add_argument("--model_name", default="LSTM", type=str)
parser.add_argument("--use_attention", action="store_true")
parser.add_argument("--hidden_size", default=50, type=int)
parser.add_argument("--num_layers", default=2, type=int)
parser.add_argument("--num_directions", default=2, type=int)
parser.add_argument("--embedding_dim", default=11, type=int)

##### Dataset params
parser.add_argument("--dataset", default="testground score components", type=str)
parser.add_argument("--window_size", default=5, type=int)
parser.add_argument("--stride", default=1, type=int)

##### Input params
parser.add_argument("--feature_type", default="sequentials", type=str, choices=["sequentials", "semantics"])
parser.add_argument("--label_type", default="next_log", type=str)
parser.add_argument("--use_tfidf", action="store_true")
parser.add_argument("--max_token_len", default=50, type=int)
parser.add_argument("--min_token_count", default=1, type=int)

##### Training params
parser.add_argument("--epoches", default=10, type=int)
parser.add_argument("--batch_size", default=100, type=int)
parser.add_argument("--learning_rate", default=0.01, type=float)
parser.add_argument("--topk", default=11, type=int)
parser.add_argument("--patience", default=4, type=int)

##### Others
parser.add_argument("--random_seed", default=42, type=int)
parser.add_argument("--gpu", default=0, type=int)

args, unknown = parser.parse_known_args()
params = vars(args)

model_save_path = dump_params(params)


if __name__ == "__main__":
    seed_everything(params["random_seed"])
    meta_data = {'num_labels':11, 'vocab_size': 14}
    
    dataset_train = log_dataset_traces(traces)
    
    dataloader_train = DataLoader(
        dataset_train, batch_size=params["batch_size"], shuffle=True, pin_memory=True
    )

    dataset_test = log_dataset_traces(traces_anomaly)
    dataloader_test = DataLoader(
        dataset_test, batch_size=1, shuffle=False, pin_memory=True
    )

    model = LSTM(meta_data=meta_data, model_save_path=model_save_path, **params)

    eval_results = model.fit(
        dataloader_train,
        test_loader=dataloader_test,
        epoches=params["epoches"],
        learning_rate=params["learning_rate"],
    )

    result_str = "\t".join(["{}-{:.4f}".format(k, v) for k, v in eval_results.items()])

    key_info = [
        "dataset",
        "train_anomaly_ratio",
        "feature_type",
        "label_type",
        "use_attention",
    ]

    args_str = "\t".join(
        ["{}:{}".format(k, v) for k, v in params.items() if k in key_info]
    )

    dump_final_results(params, eval_results, model)
