import app
from ml.data.prepare import choose_random_stock_codes
from ml.lstm3.FundFlowDataset import FundFlowDataset
from ml.lstm3.LSTM3Factory import LSTM3Factory
from ml.lstm4.LSTM4Factory import LSTM4Factory
from ml.lstm4.VXXDataset import VXXDataset
from sklearn.metrics import mean_absolute_error

if __name__ == '__main__':
    # factory1 = LSTM4Factory(batch_size=1)
    # model = factory1.model
    # model.summary()
    #
    #
    # factory1.save()
    # factory1.load()
    # #
    # ds = factory1.data_set
    # X,y = ds.get_data_set()
    # model.fit(X,y)
    # predict_y = model.predict(X)
    # print(predict_y)
    # factory1.save()
    # factory1.load()
    #
    # X,y = ds.get_data_set()
    # model.fit(X,y)
    # predict_y = model.predict(X)
    # print(predict_y)


    # codes = choose_random_stock_codes(100)
    # ds1 = VXXDataset()
    # X1, y1 = ds1.get_test_data_by_codes(codes)
    # factory1 = LSTM4Factory(path='../../model_data/lstm4_3')
    # model1 = factory1.model
    # predict_y1 = model1.predict(X1)
    #
    # ds2 = FundFlowDataset()
    # X2, y2 = ds2.get_test_data_by_codes(codes)
    # factory2 = LSTM3Factory(path='../../model_data/lstm3_3')
    # model2 = factory2.model
    # predict_y2 = model2.predict(X2)
    #
    # res1 = mean_absolute_error(predict_y1, y1)
    # res2 = mean_absolute_error(predict_y2, y2)
    #
    # print(res1)
    # print(res2)

    codes = choose_random_stock_codes(500)
    ds1 = VXXDataset(mask_size=1)
    X1, y1 = ds1.get_test_data_by_codes(codes)
    factory1 = LSTM4Factory(path='../../model_data/lstm4_1')
    model1 = factory1.model
    predict_y1 = model1.predict(X1)

    ds2 = FundFlowDataset(mask_size=1)
    X2, y2 = ds2.get_test_data_by_codes(codes)
    factory2 = LSTM3Factory(path='../../model_data/lstm3_1')
    model2 = factory2.model
    predict_y2 = model2.predict(X2)

    res1 = mean_absolute_error(predict_y1, y1)
    res2 = mean_absolute_error(predict_y2, y2)

    print(res1)
    print(res2)

