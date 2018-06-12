class Neuron:
	eta= 0.001
	alpha= 0.01
	def __init__(self, layer):
		self.dendrons= []
		self.error= 0.0
		self.gradient= 0.0
		self.output= 0.0
		if layer is None:
			pass
		else:
			for neuron in layer:
				con= Connection(neuron)
				self.dendrons.append(con)
