import torch
from model import FetchPolicy

model = FetchPolicy()
dummy_obs = torch.randn(1, 50)

torch.save(model.state_dict(), "fetch_policy.pt")
print("Model saved: fetch_policy.pt")
