from log import log
from ml.get_factory import get_factory
from ml.plugins.tensorboard_callback import get_tensor_board_callback
from task_manager import task_manager


@task_manager.celery.task()
def training_model(model_name='lstm', predict_day=3, batch_size=10, *args, **kwargs):
    Factory = get_factory(model_name)
    factory = Factory(predict_day=predict_day)
    ds = factory.data_set
    model = factory.model
    for i in range(batch_size):
        try:
            X, y = ds.get_data_set()
            model.fit(
                X, y,
                batch_size=1000,
                epochs=4,
                callbacks=[get_tensor_board_callback()],
                verbose=0,
            )
            factory.save()
            log.info(f"training No {i},saved!")

        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
