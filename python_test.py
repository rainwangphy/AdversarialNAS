import torch

aaa = torch.rand((3, 5))

print(aaa[:5].view(-1))
print(aaa[:5].reshape(-1))