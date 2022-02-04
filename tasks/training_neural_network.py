from pandas import DataFrame

from log import log
from ml.nn2.NeuralNetworkFactory import NeuralNetworkFactory
from ml.nn2.model import get_early_stop_callback
from task_manager import task_manager


@task_manager.celery.task()
def training_neural_network(predict_day=3, batch_size=10):
    factory = NeuralNetworkFactory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    testing_X, testing_y = ds.get_test_data_set()
    early_stopping = get_early_stop_callback()
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            history = model.fit(
                X.tolist(), y,
                validation_data=(testing_X.tolist(), testing_y),
                batch_size=100,
                epochs=10,
                callbacks=[early_stopping],
                verbose=0,
            )
            # verify
            history_df = DataFrame(history.history)
            log.info("Minimum validation loss: {}".format(history_df['val_loss'].min()))
            # save to file
            factory.save()
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
