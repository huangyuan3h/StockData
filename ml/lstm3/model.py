from tensorflow.keras import layers, callbacks, Sequential


def get_lstm3_model(n_steps=60, n_features=14, lstm_layer_size=1024):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features)),
        layers.LSTM(512, return_sequences=True),
        layers.LSTM(256, return_sequences=True),
        layers.LSTM(128, return_sequences=False),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(64, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(32, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model

