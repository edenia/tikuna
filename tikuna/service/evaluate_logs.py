import sys
sys.path.append("../")
import argparse
import pandas as pd
from torch.utils.data import DataLoader
from tikuna.models import LSTM
from tikuna.common.preprocess import FeatureExtractor
from tikuna.common.dataloader import load_sessions, log_dataset
from tikuna.common.utils import seed_everything, dump_final_results, dump_params, load_params

class EthereumAttackDetector():
    def __init__():
        self.params, self.meta_data = load_params("current")
        self.params["cache"] = True

        self.ext = FeatureExtractor(**params)

        session_test = ext.fit_transform(evaluation_data, datatype="test")
        dataset_test = log_dataset(session_test, feature_type=params["feature_type"])
        dataloader_test = DataLoader(
            dataset_test, batch_size=100, shuffle=False, pin_memory=True
        )

        self.model_save_path = dump_params(params, meta_data)
        self.model = LSTM(meta_data=meta_data, model_save_path=model_save_path, **params)
        self.model.label_type = "anomaly"

def evaluate():
   final_test_results = model.evaluate(
        dataloader_test,
        dtype="evaluate"
   )
