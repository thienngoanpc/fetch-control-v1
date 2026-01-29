import torch
import torch.nn as nn

class FetchPolicy(nn.Module):
    def __init__(self, obs_dim=50, action_dim=13):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Tanh()   # output in [-1, 1]
        )

    def forward(self, obs):
        return self.net(obs)
