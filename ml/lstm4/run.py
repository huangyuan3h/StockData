import app
from sklearn.metrics import mean_absolute_error

from ml.data.prepare import choose_random_stock_codes
from ml.lstm4.LSTM4Factory import LSTM4Factory
from ml.lstm4.VXXDataset import VXXDataset


def verify_model(code_num=500, mask_size=3, paths=[]):
    codes = choose_random_stock_codes(code_num)
    ds = VXXDataset(mask_size=mask_size)
    X, y = ds.get_test_data_by_codes(codes)

    for path in paths:
        factory = LSTM4Factory(path=path)
        model = factory.model
        predict_y = model.predict(X)
        res = mean_absolute_error(predict_y, y)
        print(res)


if __name__ == '__main__':
    """
    lstm4_3 data vs lstm4_3 checkpoint
    """
    # verify_model(code_num=500, mask_size=3,
    #              paths=['../../model_data/lstm4_3',
    #                     '../../model_data/lstm4_3_checkpoint_0328',
    #                     '../../model_data/lstm4_3_checkpoint_0330'])

    """
    lstm4_1 data vs lstm4_1 checkpoint
    """
    # verify_model(code_num=500, mask_size=1,
    #              paths=['../../model_data/lstm4_1',
    #                     '../../model_data/lstm4_1_checkpoint_0306',
    #                     '../../model_data/lstm4_1_checkpoint_0315'])

    verify_model(code_num=300, mask_size=5,
                 paths=['../../model_data/lstm4_5',
                        '../../model_data/lstm4_5_checkpoint_0401',
                        ])
