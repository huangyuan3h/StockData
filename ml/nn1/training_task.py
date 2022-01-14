import app
from ml.nn1.StockListDataset import StockListDataset


def run_training():
    stock_dataset = StockListDataset()
    stock_dataset.generate_training_data_and_labels()

    print(stock_dataset.data)
    print(stock_dataset.labels)



if __name__ == '__main__':
    run_training()
