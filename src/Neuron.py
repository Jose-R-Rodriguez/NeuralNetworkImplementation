class Neuron:
	eta= 0.001
	alpha= 0.01
	def __init__(self, layer):
		#dendrons are connections
		self.dendrons= []
		#Error distribution
		self.error= 0.0
		self.gradient= 0.0
		self.output= 0.0
		if layer is None:
			pass
		else:
			for neuron in layer:
				con= Connection(neuron)
				self.dendrons.append(con)
	def addError(self, err):
		self.error+= err

	def sigmoid(self, x):
		return 1 / (1 + math.exp(-x * 1.0))

	def dSigmoid(self, x):
		return x * (1.0 - x)

	def setError(self, err):
		self.error= err

	def setOutput(self, output):
		self.output= output

	def getOutput(self):
		return self.output

	def feedForward(self):
		sumOutput= 0
		if not self.dendrons:
			return
		for dendron in self.dendrons:
			sumOutput+= dendron.connectedNeuron.getOutput() * dendron.weight
		self.output= self.sigmoid(sumOutput)

	def backPropagate(self):
		self.gradient= self.error * self.dSigmoid(self.output)
		for dendron in self.dendrons:
			dendron.dWeight = Neuron.eta * (
			dendron.connectedNeuron.output * self.gradient) + self.alpha * dendron.dWeight
			dendron.weight = dendron.weight + dendron.dWeight
			dendron.connectedNeuron.addError(dendron.weight * self.gradient)
		self.error = 0
