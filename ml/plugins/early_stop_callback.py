from tensorflow import keras


def get_early_stop_callback(min_delta=0.01, patience=20):
    early_stopping = keras.callbacks.EarlyStopping(
        min_delta=min_delta,  # minimium amount of change to count as an improvement
        patience=patience,  # how many epochs to wait before stopping
        restore_best_weights=True,
    )
    return early_stopping
