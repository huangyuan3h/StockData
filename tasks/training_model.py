from log import log
from ml.get_factory import get_factory
from ml.plugins.check_point_callback import get_check_point_callback
from ml.plugins.tensorboard_callback import get_tensor_board_callback, named_logs
from task_manager import task_manager


def training_model_v2(model_name='lstm4', predict_day=3, batch_size=10, *args, **kwargs):
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    testing_X, testing_y = ds.get_test_data_set()
    tensorboard = get_tensor_board_callback(model_name, predict_day)
    tensorboard.set_model(model)
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            log.info(f"training No {i},got all the data")
            logs1 = model.train_on_batch(X, y)
            logs2 = model.test_on_batch(testing_X, testing_y)
            tensorboard.on_train_batch_end(i, named_logs(model, logs1))
            tensorboard.on_test_batch_end(i, named_logs(model, logs2))
            factory.save()
            log.info(f"training No {i},saved!")
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")


@task_manager.celery.task()
def training_model(model_name='lstm', predict_day=3, batch_size=10, *args, **kwargs):
    if model_name == 'lstm4':
        training_model_v2(model_name, predict_day, batch_size)
        return
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    testing_X, testing_y = ds.get_test_data_set()
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            log.info(f"training No {i},got all the data")
            model.fit(
                X, y,
                batch_size=10,
                epochs=10,
                validation_data=(testing_X, testing_y),
                callbacks=[get_tensor_board_callback(model_name=model_name, predict_day=predict_day),
                           get_check_point_callback(model_name=model_name, predict_day=predict_day)],
                verbose=0,
            )
            factory.save()
            log.info(f"training No {i},saved!")

        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
