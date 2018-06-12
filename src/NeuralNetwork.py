class Network:
	def __init__(self, topology):
#topology is a list containing [input_layer,hidden_layers,output_layer]
		self.layers= []
		for numNeuron in topology:
			layer= []
			for i in range(numNeuron):
				#we got no layers then
				if not self.layers:
					layer.append(Neuron(None))
				else:
					layer.append(Neuron(self.layers[-1]))
			layer.append(Neuron(None)) #this is our bias neuron
			layer[-1].setOutput(1)		#our bias will be of 1
			self.layers.append(layer)

	def setInput(self, inputs):
		for i in range(len(inputs)):
			self.layers[0][i].setOutput(inputs[i])
