import numpy
from ml.data.prepare import get_stock_data_greater_then_min_size, get_stock_data_by_size, get_change_by_mask_size, \
    normalize_stock_data


class DecisionTreeDataset(object):

    def __init__(self, chart_size=60, mask_size=10, batch_size=1000):
        self.chart_size = chart_size
        self.mask_size = mask_size
        self.batch_size = batch_size
        self.min_training_size = chart_size + mask_size

        self.percentage_labels = []
        self.train_data = []

    def get_data_set(self):
        while len(self.percentage_labels) < self.batch_size:
            df = get_stock_data_greater_then_min_size(self.min_training_size, 500)
            loop_count = len(df.id) - self.min_training_size
            for offset in range(loop_count):
                if len(self.percentage_labels) == self.batch_size:
                    break
                df2 = get_stock_data_by_size(df, self.min_training_size, offset)
                percentage = get_change_by_mask_size(df2, self.mask_size, offset)
                train_df = df2[self.mask_size:]
                normalized_data = normalize_stock_data(train_df)
                nd_data = normalized_data.to_numpy()
                self.train_data.append(nd_data)
                self.percentage_labels.append(percentage)

        dataset = numpy.array(self.train_data)
        column, nx, ny = dataset.shape
        reshaped_data = dataset.reshape(column, nx * ny)
        return reshaped_data, self.percentage_labels


