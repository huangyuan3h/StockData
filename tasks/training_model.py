from log import log
from ml.BaseModelFactory import BaseModelFactory
from ml.data.verify import verify_model
from ml.get_factory import get_factory
from ml.plugins.check_point_callback import get_check_point_callback
from ml.plugins.early_stop_callback import get_early_stop_callback
from ml.plugins.tensorboard_callback import get_tensor_board_callback
from task_manager import task_manager


def save_model(factory: BaseModelFactory, num=0) -> bool:
    res = verify_model(factory, code_num=50)
    if res > 0:
        factory.save()
        log.info(f"training No {num},saved with mse{res}")
        return True
    return False


def init_model(model_name='lstm', predict_day=3):
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    return ds, model, factory


@task_manager.celery.task()
def training_model(model_name='lstm', predict_day=3, batch_size=10, *args, **kwargs):
    ds, model, factory = init_model(model_name=model_name, predict_day=predict_day)
    # testing_X, testing_y = ds.get_test_data_set()
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            log.info(f"training No {i},got all the data.")
            model.fit(
                X, y,
                batch_size=20,
                epochs=30,
                validation_split=0.3,
                # validation_data=(testing_X, testing_y),
                callbacks=[get_tensor_board_callback(model_name=model_name, predict_day=predict_day),
                           # get_check_point_callback(model_name=model_name, predict_day=predict_day),
                           get_early_stop_callback(min_delta=0.00005, patience=2)
                           ],
                verbose=0,
                shuffle=True
            )
            res = save_model(factory, i)
            if not res:
                ds, model, factory = init_model(model_name=model_name, predict_day=predict_day)
                log.info(f"restore the previous model!!!")

        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
