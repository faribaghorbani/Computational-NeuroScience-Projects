from pymonntorch import *

class Izhikevich(Behavior):
    def initialize(self, neurons):
        super().initialize(neurons)
        self.a = self.parameter("a", None)
        self.b = self.parameter("b", None)
        self.c = self.parameter("c", None)
        self.d = self.parameter("d", None)
        self.u = self.parameter("u", None)
        self.v = self.parameter("v", None)
        self.u_rest = self.parameter("u_rest", None)
        self.threshold = 30

    # def forward(self, neurons):