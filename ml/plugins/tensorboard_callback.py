from datetime import datetime

from tensorflow import keras


def get_tensor_board_callback(model_name: str, predict_day: str):
    time_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = f"logs/fit/{model_name}_{predict_day}_{time_stamp}"
    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
    return tensorboard_callback


def named_logs(model, logs):
    result = {}
    for l in zip(model.metrics_names, logs):
        result[l[0]] = l[1]
    return result
