from pymonntorch import *
from time_resolution import TimeResolution 
import torch
from izhikevich import Izhikevich
from constant_current import ConstantCurrent
import matplotlib.pyplot as plt


settings = {"def_type": torch.float32, "device": 'cpu', "synapse_mode": SxD}
net = Network(behavior={1: TimeResolution(dt=1)}, settings=settings)

neuron_pop1 = NeuronGroup(size=1,
                          net=net,
                          behavior={1: ConstantCurrent(i=10),
                                    3: Izhikevich(a=0.02,
                                                  b=0.2,
                                                  c=-50,
                                                  d=2,
                                                  v_rest=-55,
                                                  ),
                                    9: Recorder(tag="neuron_pop1", variables=["v"])
                                    })

net.initialize()
net.simulate_iterations(300)

plt.plot(net["neuron_pop1", 0].variables["v"][:,:])
plt.show()