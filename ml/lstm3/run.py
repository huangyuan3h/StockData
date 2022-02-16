import app
from ml.lstm3.FundFlowDataset import FundFlowDataset

if __name__ == '__main__':

    ds = FundFlowDataset()
    df = ds.get_today_df_by_code("SZ002594")

