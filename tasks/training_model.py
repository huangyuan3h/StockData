import keras.backend as K

from log import log
from ml.get_factory import get_factory
from ml.plugins.check_point_callback import get_check_point_callback
from ml.plugins.early_stop_callback import get_early_stop_callback
from ml.plugins.tensorboard_callback import get_tensor_board_callback
from task_manager import task_manager


@task_manager.celery.task()
def training_model(model_name='lstm', predict_day=3, batch_size=10, *args, **kwargs):
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    # testing_X, testing_y = ds.get_test_data_set()
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            log.info(f"training No {i},got all the data")
            model.fit(
                X, y,
                batch_size=20,
                epochs=30,
                validation_split=0.3,
                # validation_data=(testing_X, testing_y),
                callbacks=[get_tensor_board_callback(model_name=model_name, predict_day=predict_day),
                           get_check_point_callback(model_name=model_name, predict_day=predict_day),
                           get_early_stop_callback()
                           ],
                verbose=0,
                shuffle=True
            )
            factory.save()
            learning_rate = K.eval(model.optimizer.lr)
            log.info(f"training No {i},saved! learning_rate: {learning_rate}")

        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
