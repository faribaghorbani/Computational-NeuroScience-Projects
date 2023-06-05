from pymonntorch import *

class ConstantCurrent(Behavior):
    def initialize(self, neurons):
        self.i = self.parameter("i", None)
        neurons.I = neurons.vector(self.i)

    def forward(self, neurons):
        neurons.I = neurons.vector(self.i)