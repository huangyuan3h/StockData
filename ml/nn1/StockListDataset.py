import torch
from pandas import DataFrame
from torch.utils.data import Dataset

from ml.data.prepare import get_stock_data_by_size, get_stock_data_greater_then_min_size, get_change_by_mask_size

"""

this ml is to find the next 10 day will get big interest

so we need 70 records
"""


def normalize_data(data):

    return_data = data.copy()
    ## delete code id timestamp
    del return_data['id']
    del return_data['code']
    del return_data['timestamp']

    return_data['volume'] = data['volume'] / 10 ** 5
    return_data['amount'] = data['amount'] / 10 ** 7
    return_data['market_capital'] = data['market_capital'] / 10 ** 9

    return return_data


class StockListDataset(Dataset):
    data = []  # training data
    labels = []  # labels

    def __init__(self, chart_size=60, predict_after_size=10, total_size=1000):
        self.chart_size = chart_size
        self.predict_after_size = predict_after_size
        self.min_training_size = chart_size + predict_after_size
        self.total_size = total_size

    def get_training_dataframe(self, df: DataFrame):
        return df[self.predict_after_size:]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        label = self.labels[idx]
        data = self.data[idx]
        return data.float(), label.float()

    def generate_training_data_and_labels(self):

        while len(self.labels) < self.total_size:
            df = get_stock_data_greater_then_min_size(self.min_training_size)

            loop_count = len(df.id) - self.min_training_size

            for offset in range(loop_count):
                if len(self.labels) == self.total_size:
                    break
                df2 = get_stock_data_by_size(df, self.min_training_size, offset)
                percentage = get_change_by_mask_size(df2, self.predict_after_size, offset)
                training_data = self.get_training_dataframe(df2)

                ## normalize
                training_data = normalize_data(training_data)

                numpy_result = training_data.to_numpy()

                tensor_result = torch.from_numpy(numpy_result)
                self.data.append(tensor_result)
                self.labels.append(torch.tensor([percentage]))
