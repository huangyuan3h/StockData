from tensorflow.keras import layers, Sequential, optimizers, losses, metrics


def get_lstm5_model(n_steps=60, n_features=23, lstm_layer_size=100):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features)),
        layers.LSTM(50, return_sequences=False),
        layers.Dense(25, activation='elu'),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model

