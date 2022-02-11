from pandas import DataFrame

from log import log
from ml.get_factory import get_factory
from ml.plugins.early_stop_callback import get_early_stop_callback
from ml.plugins.tensorboard_callback import tensorboard_callback
from task_manager import task_manager


@task_manager.celery.task()
def training_lstm(model_name='lstm', predict_day=3, batch_size=10):
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    testing_X, testing_y = ds.get_test_data_set()
    early_stopping = get_early_stop_callback()
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            history = model.fit(
                X, y,
                validation_data=(testing_X, testing_y),
                batch_size=1000,
                epochs=100,
                callbacks=[early_stopping, tensorboard_callback],
                verbose=0,
            )
            # verify
            history_df = DataFrame(history.history)
            log.info(f"training No {i}, Minimum validation loss: {history_df['val_loss'].min()}")
            # save to file
            factory.save()
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
