

def get_factory(model_name='lstm'):
    from ml.lstm.LSTMFactory import LSTMFactory
    from ml.lstm2.LSTM2Factory import LSTM2Factory
    from ml.lstm3.LSTM3Factory import LSTM3Factory
    from ml.lstm4.LSTM4Factory import LSTM4Factory

    if model_name == 'lstm':
        return LSTMFactory
    if model_name == 'lstm2':
        return LSTM2Factory
    if model_name == 'lstm3':
        return LSTM3Factory
    if model_name == 'lstm4':
        return LSTM4Factory
