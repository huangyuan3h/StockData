

def get_factory(model_name='lstm'):
    from ml.lstm.LSTMFactory import LSTMFactory
    from ml.lstm2.LSTMFactory import LSTM2Factory
    if model_name == 'lstm':
        return LSTMFactory
    if model_name == 'lstm2':
        return LSTM2Factory
