import app
from ml.nn2.NeuralNetworkFactory import NeuralNetworkFactory

if __name__ == '__main__':
    factory = NeuralNetworkFactory(predict_day=3, path='../../model_data/neuralNetwork_3.tf')
    ds = factory.data_set
    X, y = ds.get_data_set()
    print(X.shape)
