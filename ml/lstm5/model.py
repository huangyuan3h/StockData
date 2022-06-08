from tensorflow.keras import layers, Sequential, optimizers, losses, metrics



def get_lstm5_model(n_steps=60, n_features=23, lstm_layer_size=4096):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features), name="lstm1"),
        layers.LSTM(2048, return_sequences=True, name="lstm2"),
        layers.LSTM(1024, return_sequences=True, name="lstm3"),
        layers.LSTM(512, return_sequences=True, name="lstm4"),
        layers.LSTM(256, return_sequences=False, name="lstm5"),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(256, activation='elu', name="dense1"),
        layers.BatchNormalization(),
        layers.Dropout(0.1),
        layers.Dense(128, activation='elu', name="dense2"),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model
