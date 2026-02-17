import torch
import torch.nn as nn

class DepthModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 4)

    def forward(self):
        x = torch.rand(1, 1)
        return self.fc(x)
