import sys
sys.path.append("../")
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
import argparse
import pandas as pd
from torch.utils.data import DataLoader
from tikuna.models import LSTM
from tikuna.common.dataloader import load_sessions, log_dataset, log_dataset_octets
from tikuna.common.utils import seed_everything, dump_final_results, dump_params

NORMAL_LOG_DATA="/home/tikuna/app/data/mainnet/normal/log/normal.log"
ECLIPSE_LOG_DATA="/home/tikuna/app/data/mainnet/eclipse-single/log/eclipse.log"

normal_data = pd.read_csv(NORMAL_LOG_DATA,
                         sep = '\s+',
                         names=["Timestamp", "Removed IP", "Removed Port",
                                "Added IP", "Added Port", "Bucket", "label"])

abnormal_data = pd.read_csv(ECLIPSE_LOG_DATA,
                         sep = '\s+',
                         names=["Timestamp", "Removed IP", "Removed Port",
                                "Added IP", "Added Port", "Bucket", "label"])

normal_data['Timestamp'] = pd.to_datetime(normal_data['Timestamp'],
                                          format='[%Y-%m-%d|%H:%M:%S.%f]')

abnormal_data['Timestamp'] = pd.to_datetime(abnormal_data['Timestamp'],
                                          format='[%Y-%m-%d|%H:%M:%S.%f]')

# Extract ip octets
normal_data.loc[:, 'Removed oct1'] = normal_data['Removed IP'].apply(lambda x: x.split(".")[0])
normal_data.loc[:, 'Removed oct2'] = normal_data['Removed IP'].apply(lambda x: x.split(".")[1])
normal_data.loc[:, 'Removed oct3'] = normal_data['Removed IP'].apply(lambda x: x.split(".")[2])
normal_data.loc[:, 'Removed oct4'] = normal_data['Removed IP'].apply(lambda x: x.split(".")[3])
normal_data.loc[:, 'Added oct1'] = normal_data['Added IP'].apply(lambda x: x.split(".")[0])
normal_data.loc[:, 'Added oct2'] = normal_data['Added IP'].apply(lambda x: x.split(".")[1])
normal_data.loc[:, 'Added oct3'] = normal_data['Added IP'].apply(lambda x: x.split(".")[2])
normal_data.loc[:, 'Added oct4'] = normal_data['Added IP'].apply(lambda x: x.split(".")[3])

abnormal_data.loc[:, 'Removed oct1'] = abnormal_data['Removed IP'].apply(lambda x: x.split(".")[0])
abnormal_data.loc[:, 'Removed oct2'] = abnormal_data['Removed IP'].apply(lambda x: x.split(".")[1])
abnormal_data.loc[:, 'Removed oct3'] = abnormal_data['Removed IP'].apply(lambda x: x.split(".")[2])
abnormal_data.loc[:, 'Removed oct4'] = abnormal_data['Removed IP'].apply(lambda x: x.split(".")[3])
abnormal_data.loc[:, 'Added oct1'] = abnormal_data['Added IP'].apply(lambda x: x.split(".")[0])
abnormal_data.loc[:, 'Added oct2'] = abnormal_data['Added IP'].apply(lambda x: x.split(".")[1])
abnormal_data.loc[:, 'Added oct3'] = abnormal_data['Added IP'].apply(lambda x: x.split(".")[2])
abnormal_data.loc[:, 'Added oct4'] = abnormal_data['Added IP'].apply(lambda x: x.split(".")[3])

training_data = {}
testing_data = {}

columns = ['Removed oct1', 'Removed oct2', 'Removed oct3', 'Removed oct4',
           'Removed Port', 'Added oct1', 'Added oct2', 'Added oct3',
           'Added oct4', 'Added Port', 'Bucket']

training_data["features"] = normal_data.loc[:1000000, columns].copy()
training_data["label"] = normal_data.iloc[:1000000, [6]].replace("normal", 0).copy()

testing_data["features"] = pd.concat([abnormal_data.loc[:, columns],
                                      normal_data.loc[1000000:1002000, columns]]).copy()
testing_data["label"] = pd.concat([
                           abnormal_data.iloc[:, [6]].replace("abnormal", 1),
                           normal_data.iloc[1000000:1002000, [6]].replace("normal", 0)]).copy()

parser = argparse.ArgumentParser()

##### Model params
parser.add_argument("--model_name", default="LSTM", type=str)
parser.add_argument("--use_attention", action="store_true")
parser.add_argument("--hidden_size", default=30, type=int)
parser.add_argument("--num_layers", default=2, type=int)
parser.add_argument("--num_directions", default=2, type=int)
parser.add_argument("--embedding_dim", default=11, type=int)

##### Dataset params
parser.add_argument("--dataset", default="Ethereum logs", type=str)
parser.add_argument("--window_size", default=20, type=int)
parser.add_argument("--stride", default=1, type=int)

##### Input params
parser.add_argument("--feature_type", default="sequentials", type=str, choices=["sequentials", "semantics"])
parser.add_argument("--label_type", default="next_vector", type=str)
parser.add_argument("--use_tfidf", action="store_true")
parser.add_argument("--max_token_len", default=50, type=int)
parser.add_argument("--min_token_count", default=1, type=int)
parser.add_argument("--cache", default="True", type=bool)

##### Training params
parser.add_argument("--epoches", default=100, type=int)
parser.add_argument("--batch_size", default=1024, type=int)
parser.add_argument("--learning_rate", default=0.01, type=float)
parser.add_argument("--topk", default=5, type=int)
parser.add_argument("--patience", default=10, type=int)

##### Others
parser.add_argument("--random_seed", default=42, type=int)
parser.add_argument("--gpu", default=0, type=int)

args, unknown = parser.parse_known_args()
params = vars(args)

model_save_path = dump_params(params, None)

seed_everything(params["random_seed"])
meta_data = {'num_labels':11, 'vocab_size': 14}

dataset_train = log_dataset_octets(training_data["features"], training_data["label"])

dataloader_train = DataLoader(
    dataset_train, batch_size=params["batch_size"], shuffle=True, pin_memory=True
)

dataset_test = log_dataset_octets(testing_data["features"], testing_data["label"])

dataloader_test = DataLoader(
    dataset_test, batch_size=1, shuffle=True, pin_memory=True
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
