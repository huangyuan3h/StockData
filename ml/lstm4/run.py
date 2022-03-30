import app
from ml.data.prepare import choose_random_stock_codes
from ml.lstm4.LSTM4Factory import LSTM4Factory
from ml.lstm4.VXXDataset import VXXDataset
from sklearn.metrics import mean_absolute_error

if __name__ == '__main__':

    """
    lstm4_3 data vs lstm4_3 checkpoint

    """

    codes = choose_random_stock_codes(300)
    ds1 = VXXDataset()
    X1, y1 = ds1.get_test_data_by_codes(codes)
    factory1 = LSTM4Factory(path='../../model_data/lstm4_3')
    model1 = factory1.model
    predict_y1 = model1.predict(X1)

    factory2 =LSTM4Factory(path='../../model_data/lstm4_3_checkpoint_0326')
    model2 = factory2.model
    predict_y2 = model2.predict(X1)

    factory3 =LSTM4Factory(path='../../model_data/lstm4_3_checkpoint_0328')
    model3 = factory3.model
    predict_y3 = model3.predict(X1)

    res1 = mean_absolute_error(predict_y1, y1)
    res2 = mean_absolute_error(predict_y2, y1)
    res3 = mean_absolute_error(predict_y3, y1)

    print(res1)
    print(res2)
    print(res3)

    """
    lstm4_1 data vs lstm4_1 checkpoint

    """

    # codes = choose_random_stock_codes(500)
    # ds1 = VXXDataset(mask_size=1)
    # X1, y1 = ds1.get_test_data_by_codes(codes)
    # factory1 = LSTM4Factory(path='../../model_data/lstm4_1')
    # model1 = factory1.model
    # predict_y1 = model1.predict(X1)
    #
    # factory2 =LSTM4Factory(path='../../model_data/lstm4_1_checkpoint_0306')
    # model2 = factory2.model
    # predict_y2 = model2.predict(X1)

    # factory3 =LSTM4Factory(path='../../model_data/lstm4_1_checkpoint_0313')
    # model3 = factory3.model
    # predict_y3 = model3.predict(X1)

    # res1 = mean_absolute_error(predict_y1, y1)
    # res2 = mean_absolute_error(predict_y2, y1)
    # res3 = mean_absolute_error(predict_y3, y1)

    # print(res1)
    # print(res2)
    # print(res3)

