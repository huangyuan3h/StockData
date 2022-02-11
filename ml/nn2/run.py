from pandas import DataFrame

import app
from ml.data.prepare import reshape_data_to_1_d
from ml.nn2.NeuralNetworkFactory import NeuralNetworkFactory
from ml.plugins.early_stop_callback import get_early_stop_callback

if __name__ == '__main__':
    factory = NeuralNetworkFactory(predict_day=3, path='../../model_data/neuralNetwork_3.tf')
    ds = factory.data_set
    X, y = ds.get_data_set()
    testing_X, testing_y = ds.get_test_data_set()
    early_stopping = get_early_stop_callback()
    model = factory.model

    history = model.fit(
        reshape_data_to_1_d(X), y,
        validation_data=(reshape_data_to_1_d(testing_X), testing_y),
        batch_size=100,
        epochs=10,
        callbacks=[early_stopping],
        verbose=0,
    )

    history_df = DataFrame(history.history)
    history_df.loc[:, ['loss', 'val_loss']].plot()
    print("Minimum validation loss: {}".format(history_df['val_loss'].min()))

