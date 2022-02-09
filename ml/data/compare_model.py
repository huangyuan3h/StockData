from pandas import DataFrame
import matplotlib.pyplot as plt

import app
# also consider
# http://data.eastmoney.com/zjlx/002594.html
from ml.data.BaseDataset import BaseDataset
from ml.lstm.LSTMFactory import LSTMFactory
from ml.lstm.model import get_early_stop_callback
from ml.lstm2.LSTMFactory import LSTM2Factory

if __name__ == '__main__':
    ds = BaseDataset(testing_batch_size=100)
    testing_X, testing_y = ds.get_test_data_set()
    early_stopping = get_early_stop_callback()
    X, y = ds.get_data_set()
    factory1 = LSTMFactory( new_model=True)
    factory2 = LSTM2Factory(new_model=True)

    model1 = factory1.model
    model2 = factory2.model

    history1 = model1.fit(
        X, y,
        validation_data=(testing_X, testing_y),
        batch_size=1000,
        epochs=100,
        callbacks=[early_stopping],
        verbose=0,
    )

    history2 = model2.fit(
        X, y,
        validation_data=(testing_X, testing_y),
        batch_size=1000,
        epochs=100,
        callbacks=[early_stopping],
        verbose=0,
    )
    history_df1 = DataFrame(history1.history)
    history_df2 = DataFrame(history2.history)
    print("1 Minimum validation loss: {}".format(history_df1['val_loss'].min()))
    print("2 Minimum validation loss: {}".format(history_df1['val_loss'].min()))
    history_df1.plot()
    history_df2.plot()
    plt.figure()

