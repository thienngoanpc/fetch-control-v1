import torch
from model import FetchPolicy

model = FetchPolicy()
torch.save(model.state_dict(), "fetch_policy.pt")
print("Model saved")
