from pymonntorch import *
from time_resolution import TimeResolution 
import torch

settings = {"def_type": torch.float32, "device": 'cpu', "synapse_mode": SxD}
net = Network(behavior={1: TimeResolution(dt=1)}, settings=settings)
