import numpy, math
class Connection:
	def __init__(self, connectedNeuron):
		self.connectedNeuron= connectedNeuron
		self.weight= numpy.random.normal()
		self.dWeight= 0.0
