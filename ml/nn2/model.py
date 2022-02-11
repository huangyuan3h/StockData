from tensorflow.keras import layers, Sequential


def get_nn_model(shape_size=840, hidden_layer_size=2048):
    model = Sequential([
        layers.BatchNormalization(input_shape=[shape_size]),
        layers.Dense(hidden_layer_size, activation='relu'),
        layers.Dropout(0.3),
        layers.BatchNormalization(),
        layers.Dense(hidden_layer_size, activation='relu'),
        layers.Dropout(0.3),
        layers.BatchNormalization(),
        layers.Dense(hidden_layer_size, activation='relu'),
        layers.Dropout(0.3),
        layers.BatchNormalization(),
        layers.Dense(1),
    ])
    model.compile(
        optimizer='sgd',
        loss='mae',
        metrics=['mae'],
    )
    return model

