from pandas import DataFrame
import app
from ml.lstm.LSTMFactory import LSTMFactory
from ml.lstm.model import get_early_stop_callback

if __name__ == '__main__':
    factory = LSTMFactory(predict_day=3, path='../../model_data/lstm_3.tf')
    ds = factory.data_set
    X, y = ds.get_data_set()
    testing_X, testing_y = ds.get_test_data_set()
    early_stopping = get_early_stop_callback()
    model = factory.model

    history = model.fit(
        X, y,
        validation_data=(testing_X, testing_y),
        batch_size=100,
        epochs=10,
        callbacks=[early_stopping],
        verbose=0,
    )

    history_df = DataFrame(history.history)
    print("Minimum validation loss: {}".format(history_df['val_loss'].min()))


