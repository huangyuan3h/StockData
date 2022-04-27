from tensorflow.keras import layers, Sequential, optimizers, losses, metrics



def get_lstm5_model(n_steps=60, n_features=23, lstm_layer_size=2048):
    model = Sequential([
        layers.LSTM(units=lstm_layer_size, return_sequences=True, input_shape=(n_steps, n_features)),
        layers.LSTM(int(lstm_layer_size / 2 ** 2), return_sequences=False),
        layers.Dropout(0.1),
        layers.Dense(int(lstm_layer_size / 2 ** 4), activation='relu'),
        layers.Dropout(0.1),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='adam',
        loss='mae',
        metrics=['mae'],
    )
    return model
