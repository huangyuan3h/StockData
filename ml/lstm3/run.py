import app
from ml.lstm3.FundFlowDataset import get_stock_data_greater_then_min_size_with_fund_flow

if __name__ == '__main__':
    result = get_stock_data_greater_then_min_size_with_fund_flow(63,100)

