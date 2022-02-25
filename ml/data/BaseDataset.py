from pandas import DataFrame

from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size, \
    normalize_stock_data, get_stock_data


def get_data_label_by_dataframe(df: DataFrame, mask_size=10):
    percentage = get_change_by_mask_size(df, mask_size)
    train_df = df[mask_size:]
    normalized_data = normalize_stock_data(train_df)
    nd_data = normalized_data.to_numpy()
    return nd_data, percentage


class BaseDataset(object):

    def __init__(self, chart_size=60, mask_size=3, batch_size=10 ** 5, testing_batch_size=10 ** 3):
        self.chart_size = chart_size
        self.mask_size = mask_size
        self.batch_size = batch_size
        self.min_training_size = chart_size + mask_size

        self.percentage_labels = []
        self.train_data = []

        self.testing_batch_size = testing_batch_size
        self.test_labels = []
        self.testing_data = []

    def get_data_set(self):
        self.percentage_labels = []
        self.train_data = []
        while len(self.percentage_labels) < self.batch_size:
            df = get_stock_data_greater_then_min_size(self.min_training_size, 500)
            loop_count = len(df.id) - self.min_training_size
            for offset in range(loop_count):
                if len(self.percentage_labels) == self.batch_size:
                    break
                df2 = get_stock_data_by_size(df, self.min_training_size, offset)
                nd_data, percentage = get_data_label_by_dataframe(df2, self.mask_size)
                self.train_data.append(nd_data.tolist())
                self.percentage_labels.append(percentage)

        return self.train_data, self.percentage_labels

    def get_test_data_set(self):
        self.test_labels = []
        self.testing_data = []
        while len(self.test_labels) < self.testing_batch_size:
            # the close 20 day as the test data
            df = get_stock_data_greater_then_min_size(self.min_training_size, self.min_training_size + 20)
            loop_count = len(df.id) - self.min_training_size
            for offset in range(loop_count):
                if len(self.test_labels) == self.batch_size:
                    break
                df2 = get_stock_data_by_size(df, self.min_training_size, offset)
                nd_data, percentage = get_data_label_by_dataframe(df2, self.mask_size)
                self.testing_data.append(nd_data.tolist())
                self.test_labels.append(percentage)

        return self.testing_data, self.test_labels

    def get_today_df_by_code(self, code: str):
        return get_stock_data(code, self.chart_size)
