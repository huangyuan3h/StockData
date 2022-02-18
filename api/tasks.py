from api.response_code import OK


def get_task():
    from task_manager import task_manager
    celery = task_manager.celery
    inspect = celery.control.inspect()
    active = inspect.active()
    print(active)
    print(inspect.reserved())
    print(inspect.scheduled())
    print(inspect.registered())
    return OK
