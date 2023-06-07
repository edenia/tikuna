import sys
sys.path.append("../")
import argparse
import pandas as pd
import json
import os
import logging

from threading import Thread
from alertmanager import AlertManager
from alertmanager import Alert
from torch.utils.data import DataLoader
from tikuna.models import LSTM
from tikuna.common.dataloader import load_sessions, log_dataset_octets
from tikuna.common.utils import seed_everything, dump_final_results, dump_params, load_params
from tikuna.common.utils import load_scaler, save_scaler

class EthereumAttackDetector():
    def __init__(self):
        working_directory = "production"
        self.params, self.meta_data = load_params(working_directory)
        self.params["cache"] = True
        self.params["evaluation"] = True
        self.meta_data = {'num_labels':11, 'vocab_size': 14}

        save_dir = os.path.join("/home/tikuna/app/data/tikuna_model_data", working_directory)
        model_file = os.path.join(save_dir, "model.ckpt")
        os.makedirs(save_dir, exist_ok=True)

        # load scaler
        self.scaler = load_scaler(working_directory)
        if self.scaler is None:
            logging.error("MinMax Scaler file not found!")
            return

        log_file = os.path.join(save_dir, "tikuna.log")

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s P%(process)d %(levelname)s %(message)s",
            handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        )

        logging.info(json.dumps(self.params, indent=4))
        self.model = LSTM(meta_data=self.meta_data, model_save_path=save_dir, **self.params)
        self.model.load_model(model_file)

    def evaluate(self, input_json):
        evaluation_data = {}
        input_list = json.loads(input_json)
        input_data = pd.DataFrame(input_list)

        # Extract IP octets
        input_data.loc[:, 6] = input_data.iloc[:, 1].apply(lambda x: x.split(".")[0])
        input_data.loc[:, 7] = input_data.iloc[:, 1].apply(lambda x: x.split(".")[1])
        input_data.loc[:, 8] = input_data.iloc[:, 1].apply(lambda x: x.split(".")[2])
        input_data.loc[:, 9] = input_data.iloc[:, 1].apply(lambda x: x.split(".")[3])

        input_data.loc[:, 10] = input_data.iloc[:, 3].apply(lambda x: x.split(".")[0])
        input_data.loc[:, 11] = input_data.iloc[:, 3].apply(lambda x: x.split(".")[1])
        input_data.loc[:, 12] = input_data.iloc[:, 3].apply(lambda x: x.split(".")[2])
        input_data.loc[:, 13] = input_data.iloc[:, 3].apply(lambda x: x.split(".")[3])

        evaluation_data["features"] = input_data.iloc[:, [6,7,8,9,2,10,11,12,13,4,5]]
        evaluation_data["label"] = None

        # Scale evaluation data
        evaluation_data_scaled = self.scaler.transform(evaluation_data["features"].to_numpy())

        dataset_evaluation = log_dataset_octets(pd.DataFrame(evaluation_data_scaled), evaluation_data["label"])

        dataloader_test = DataLoader(
            dataset_evaluation, batch_size=200, shuffle=False, pin_memory=True
        )
        anomalies = self.model.predict_vector(dataloader_test)
        if anomalies > 0:
            print("Found anomalies!!:", anomalies)
            thread = Thread(target=self.send_alert, args=(input_json,))
            thread.start()

    def send_alert(self, message):
        alert_data = {
            "labels": {
                "alertname": "EclipseAttackOnEthereumNode",
                "instance": "localhost:4444",
                "job": "prometheus",
                "severity": "critical",
                "log_data": message
            }
        }
        alert = Alert.from_dict(alert_data)
        alert_manager = AlertManager(host="http://localhost")
        alert_manager.post_alerts(alert)
