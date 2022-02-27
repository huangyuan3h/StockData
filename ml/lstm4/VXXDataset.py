from pandas import DataFrame
from tensorflow import convert_to_tensor

from ml.data.BaseDataset import BaseDataset
from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size, \
    normalize_stock_data
from utils.dateUtils import string_to_datetime

default_limit = 100


def get_data_label_by_dataframe(df: DataFrame, mask_size=10):
    percentage = get_change_by_mask_size(df, mask_size)
    train_df = df[mask_size:]
    normalized_data = normalize_stock_data(train_df)
    nd_data = normalized_data.to_numpy()
    return nd_data, percentage


class VXXDataset(BaseDataset):

    def __init__(self, chart_size=60, mask_size=3, batch_size=1000, testing_batch_size=300):
        BaseDataset.__init__(self, chart_size=chart_size, mask_size=mask_size, batch_size=batch_size,
                             testing_batch_size=testing_batch_size)
        # index list
        from dao.index_kline_process import get_index_kline
        from dao.mapping.base_mapping import obj_2_dataframe
        all_index_df = obj_2_dataframe(get_index_kline("SH000001", default_limit))
        self.index_df = all_index_df.loc[:, ["timestamp", "percent", "turnoverrate"]]
        self.index_df.rename(columns={"percent": "index_percent", "turnoverrate": "index_turnoverrate"}, inplace=True)
        # VXX list
        all_vxx_df = obj_2_dataframe(get_index_kline("VXX", default_limit))
        self.vxx_df = all_vxx_df.loc[:, ["timestamp", "percent", "turnoverrate"]]
        self.vxx_df.rename(columns={"percent": "vxx_percent", "turnoverrate": "vxx_turnoverrate"}, inplace=True)

    def get_stock_data_greater_then_min_size_with_fund_flow(self, chart_size: int, limit: int) -> DataFrame:
        from dao.fund_flow_process import get_fund_flow_by_code
        from dao.mapping.base_mapping import obj_2_dataframe
        df = get_stock_data_greater_then_min_size(chart_size, limit)
        code = df["code"][0]
        fund_flow = obj_2_dataframe(get_fund_flow_by_code(code, limit))
        # merge fund flow to main df
        del fund_flow["code"]
        del fund_flow["id"]
        joined_df = df.set_index('timestamp').join(fund_flow.set_index('timestamp'))

        # merge the index data
        all_df = joined_df.join(self.index_df.set_index('timestamp'))
        self.vxx_df["timestamp"] = self.vxx_df["timestamp"].map(lambda x: string_to_datetime(str(x).split()[0]))
        all_df = all_df.join(self.vxx_df.set_index('timestamp'))

        # reset the place of timestamp
        all_df.reset_index(inplace=True)
        return all_df

    def get_data_set(self):
        self.percentage_labels = []
        self.train_data = []
        while len(self.percentage_labels) < self.batch_size:
            df = self.get_stock_data_greater_then_min_size_with_fund_flow(self.min_training_size, default_limit)
            loop_count = len(df.id) - self.min_training_size
            for offset in range(loop_count):
                if len(self.percentage_labels) == self.batch_size:
                    break
                df2 = get_stock_data_by_size(df, self.min_training_size, offset)
                nd_data, percentage = get_data_label_by_dataframe(df2, self.mask_size)
                self.train_data.append(nd_data.tolist())
                self.percentage_labels.append(percentage)

        return convert_to_tensor(self.train_data), convert_to_tensor(self.percentage_labels)

    def get_test_data_set(self):
        self.test_labels = []
        self.testing_data = []
        while len(self.test_labels) < self.testing_batch_size:
            # the close 1 day as the test data
            df = self.get_stock_data_greater_then_min_size_with_fund_flow(self.min_training_size,
                                                                          self.min_training_size + 1)
            loop_count = len(df.id) - self.min_training_size
            for offset in range(loop_count):
                if len(self.test_labels) == self.batch_size:
                    break
                df2 = get_stock_data_by_size(df, self.min_training_size, offset)
                nd_data, percentage = get_data_label_by_dataframe(df2, self.mask_size)
                self.testing_data.append(nd_data.tolist())
                self.test_labels.append(percentage)

        return convert_to_tensor(self.testing_data), convert_to_tensor(self.test_labels)

    def get_today_df_by_code(self, code: str):
        df = self.get_stock_data_greater_then_min_size_with_fund_flow(self.chart_size, self.chart_size)

        return df
