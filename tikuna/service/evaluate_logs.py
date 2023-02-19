import sys
sys.path.append("../")
import argparse
import pandas as pd
import json

from torch.utils.data import DataLoader
from tikuna.models import LSTM
from tikuna.common.preprocess import FeatureExtractor
from tikuna.common.dataloader import load_sessions, log_dataset
from tikuna.common.utils import seed_everything, dump_final_results, dump_params, load_params

class EthereumAttackDetector():
    def __init__(self):
        self.params, self.meta_data = load_params("current")
        self.params["cache"] = True

        self.feature_extractor = FeatureExtractor(**self.params)

        model_save_path = dump_params(self.params, self.meta_data)
        self.model = LSTM(meta_data=self.meta_data, model_save_path=model_save_path, **self.params)

    def evaluate(self, input_json):
        evaluation_data = {}
        input_list = json.loads(input_json)
        input_data = pd.DataFrame(input_list)

        evaluation_data["features"] = input_data.iloc[:, 1:6]
        session_test = self.feature_extractor.fit_transform(evaluation_data, datatype="predict")
        dataset_test = log_dataset(session_test, feature_type=self.params["feature_type"])
        dataloader_test = DataLoader(
            dataset_test, batch_size=1, shuffle=False, pin_memory=True
        )
        self.model.label_type = "anomaly"
        final_test_results = self.model.predict(dataloader_test)
