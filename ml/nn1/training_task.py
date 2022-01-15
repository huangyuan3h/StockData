from torch.utils.data import DataLoader

import app
from ml.nn1.CommonNeuralNetwork import CommonNeuralNetwork
from ml.nn1.StockListDataset import StockListDataset
import torch
from torch import nn
# Get cpu or gpu device for training.
from ml.nn1.training import train

device = "cuda" if torch.cuda.is_available() else "cpu"

def run_training():
    stock_dataset = StockListDataset()
    stock_dataset.generate_training_data_and_labels()
    model = CommonNeuralNetwork(input_shape=60*14, output_shape = 1).to(device)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)
    train_dataloader = DataLoader(stock_dataset, batch_size=30, shuffle=True)
    train(train_dataloader, model, loss_fn, optimizer)



if __name__ == '__main__':
    run_training()
