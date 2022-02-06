from ml.lstm.LSTMFactory import LSTMFactory
from ml.lstm.model import get_early_stop_callback

if __name__ == '__main__':
    factory = LSTMFactory(predict_day=3, path='../../model_data/lstm_3.tf')
    ds = factory.data_set
    X, y = ds.get_data_set()
    testing_X, testing_y = ds.get_test_data_set()
    early_stopping = get_early_stop_callback()
    model = factory.model


