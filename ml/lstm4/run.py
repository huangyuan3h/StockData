import app
from ml.lstm4.VXXDataset import VXXDataset
from ml.lstm4.model import get_lstm4_model

if __name__ == '__main__':

    #  model = get_lstm4_model()

    ds = VXXDataset()
    df = ds.get_data_set()
