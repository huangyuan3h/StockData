import app
from ml.data.prepare import choose_random_stock_codes
from ml.lstm3.FundFlowDataset import FundFlowDataset
from ml.lstm3.LSTM3Factory import LSTM3Factory
from ml.lstm4.LSTM4Factory import LSTM4Factory
from ml.lstm4.VXXDataset import VXXDataset
from sklearn.metrics import mean_absolute_error

if __name__ == '__main__':
    codes = choose_random_stock_codes(500)
    ds1 = VXXDataset()
    X1, y1 = ds1.get_test_data_by_codes(codes)
    factory1 = LSTM4Factory()
    model1 = factory1.model
    predict_y1 = model1.predict(X1)

    ds2 = FundFlowDataset()
    X2, y2 = ds2.get_test_data_by_codes(codes)
    factory2 = LSTM3Factory()
    model2 = factory2.model
    predict_y2 = model2.predict(X2)

    res1 = mean_absolute_error(predict_y1, y1)
    res2 = mean_absolute_error(predict_y2, y2)

    print(res1)
    print(res2)

