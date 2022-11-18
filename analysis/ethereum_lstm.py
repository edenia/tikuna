#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Parameters in this cell can be overriden using papermill

# path to directory contaning output from the extract_test_outputs method in analyze.py
ANALYSIS_DIR="."

# If no cached 'meshes.gz' file exists when loading data, setting
# DERIVE_MESHES to True causes the mesh state to be derived from
# trace events. This will add several minutes to the load time,
# but the results will be cached to disk.
DERIVE_MESHES=False

# When DERIVE_MESHES is true, you can change the sample frequency
# by setting MESH_SAMPLE_FREQ. This controls the size of the time window
# for each mesh "snapshot".
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
from pprint import pprint
import pathlib
import seaborn as sns
from durations import Duration

import notebook_helper
from notebook_helper import no_scores_message, load_pandas, archive_figures, p25, p50, p75, p95, p99
from torch.utils.data import DataLoader
from sklearn.preprocessing import MinMaxScaler
from tikuna.models import LSTM
from tikuna.common.preprocess import FeatureExtractor
from tikuna.common.dataloader import load_sessions, log_dataset, log_dataset_scores
from tikuna.common.utils import seed_everything, dump_final_results, dump_params

# load data
print('loading test data from ' + ANALYSIS_DIR)

tables = load_pandas(ANALYSIS_DIR, derive_meshes_if_missing=DERIVE_MESHES, mesh_sample_freq=MESH_SAMPLE_FREQ)
scores = tables['scores']
scores = scores.dropna()
scores = scores.sort_values(['timestamp', 'observer', 'peer'])

parser = argparse.ArgumentParser()

##### Model params
parser.add_argument("--model_name", default="LSTM", type=str)
parser.add_argument("--use_attention", action="store_true")
parser.add_argument("--hidden_size", default=128, type=int)
parser.add_argument("--num_layers", default=2, type=int)
parser.add_argument("--num_directions", default=2, type=int)
parser.add_argument("--embedding_dim", default=7, type=int)

##### Dataset params
parser.add_argument("--dataset", default="testground score components", type=str)
parser.add_argument("--window_size", default=10, type=int)
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
parser.add_argument("--topk", default=7, type=int)
parser.add_argument("--patience", default=10, type=int)

##### Others
parser.add_argument("--random_seed", default=42, type=int)
parser.add_argument("--gpu", default=0, type=int)

args, unknown = parser.parse_known_args()
params = vars(args)

model_save_path = dump_params(params)


if __name__ == "__main__":
    seed_everything(params["random_seed"])
    meta_data = {'num_labels':7, 'vocab_size': 14}
    
    dataset_train = log_dataset_scores(scores)
    
    dataloader_train = DataLoader(
        dataset_train, batch_size=params["batch_size"], shuffle=True, pin_memory=True
    )

    dataset_test = log_dataset_scores(scores[10000:20000])
    dataloader_test = DataLoader(
        dataset_test, batch_size=10, shuffle=False, pin_memory=True
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
