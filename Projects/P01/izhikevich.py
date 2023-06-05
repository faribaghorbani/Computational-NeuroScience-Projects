from pymonntorch import *
import torch

class Izhikevich(Behavior):
    def initialize(self, neurons):
        super().initialize(neurons)
        self.a = self.parameter("a", None)
        self.b = self.parameter("b", None)
        self.c = self.parameter("c", None)
        self.d = self.parameter("d", None)
        self.v_rest = self.parameter("v_rest", None)
        self.threshold = 30

        neurons.u = neurons.vector("zeros")
        neurons.v = neurons.vector(self.v_rest)

    def forward(self, neurons):
        deriv_v = (torch.pow(neurons.v, 2) * 0.04) + neurons.v * 5 + 140 - neurons.u + neurons.I
        deriv_u = self.a * (self.b * neurons.v - neurons.u)

        neurons.v = neurons.v + torch.mul(neurons.v, deriv_v) * neurons.network.dt
        neurons.u = neurons.u + torch.mul(neurons.u, deriv_u) * neurons.network.dt

        # finding the neurons which reach the threshold
        neurons.spike = neurons.v > self.threshold
        
        # changing the parameters according to the izhikevich condition
        neurons.v[neurons.spike] = self.c
        neurons.u[neurons.spike] = neurons.u[neurons.spike] + self.d

 
