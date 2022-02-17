from datetime import datetime

from tensorflow import keras


def get_check_point_callback(model_name: str, predict_day: int):
    time_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = f"model_data/{model_name}_{predict_day}_{time_stamp}.tf"
    tensorboard_callback = keras.callbacks.ModelCheckpoint(filepath=path, verbose=0, monitor='val_loss',
                                                           save_best_only=False, save_freq='epoch')
    return tensorboard_callback
