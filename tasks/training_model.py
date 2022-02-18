from log import log
from ml.get_factory import get_factory
from ml.plugins.check_point_callback import get_check_point_callback
from ml.plugins.tensorboard_callback import get_tensor_board_callback
from task_manager import task_manager


@task_manager.celery.task()
def training_model(model_name='lstm3', predict_day=3, batch_size=10):
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day, batch_size=batch_size)
    ds = factory.data_set
    model = factory.model
    try:
        model.fit(
            ds,
            epochs=10,
            callbacks=[get_tensor_board_callback(model_name),
                       get_check_point_callback(model_name=model_name, predict_day=predict_day)],
            verbose=0,
        )
        factory.save()
        log.info(f"training saved!")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
