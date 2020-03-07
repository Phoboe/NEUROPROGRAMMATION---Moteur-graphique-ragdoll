from math import *

class Neuron():
    def __init__(self):
        self._in = 3
        self._back = [10,10,10]
        self._out = 1
        return None

    def total(self):
        sum = 0
        for elt in self._back:
            sum += elt
        sum += self._in + self._out
        return sum

class Perceptron():
    def __init__(self):
        self.synapse = []
        self.value   = 0
        self.score   = 0
        self.func    = 0

        self.entries = []
        self.entry = 0
        self.weight  = []

        pass

    def function(self, entry, weight): # entry les sorties des perceptrons liés à celui-ci et weight le poids de chaque entrée
        sum = 0
        for elt in entry:
            sum += entry * weight * tanh(self.func)
        self.value = sum
        return sum

    pass
