import torch
from torch import nn
# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

# Define model
class CommonNeuralNetwork(nn.Module):
    def __init__(self, input_shape = 28*28, middle_shape =512, output_shape= 10 ):
        super(CommonNeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_shape, middle_shape),
            nn.ReLU(),
            nn.Linear(middle_shape, middle_shape),
            nn.ReLU(),
            nn.Linear(middle_shape, output_shape)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)
