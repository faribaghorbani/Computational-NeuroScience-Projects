from pymonntorch import *
from time_resolution import TimeResolution 
import torch
from izhikevich import Izhikevich
from constant_current import ConstantCurrent

settings = {"def_type": torch.float32, "device": 'cpu', "synapse_mode": SxD}
net = Network(behavior={1: TimeResolution(dt=1)}, settings=settings)

neuron_pop1 = NeuronGroup(size=1,
                          net=net,
                          behavior={1: ConstantCurrent(i=10),
                                    3: Izhikevich(a=0.02,
                                                  b=0.2,
                                                  c=-66,
                                                  d=8,
                                                  v_rest=-70,
                                                  v=0,
                                                  u=0),
                                    9: Recorder(tag="neuron_pop1", variables=["u"])
                                    })