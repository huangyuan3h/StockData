import app
from ml.lstm3.FundFlowDataset import FundFlowDataset

if __name__ == '__main__':

    ds = FundFlowDataset()
    ds.get_data_set()

