from datetime import datetime

from tensorflow import keras


def get_tensor_board_callback(model_name: str):
    time_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = f"logs/fit/{model_name}-{time_stamp}"
    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
    return tensorboard_callback
