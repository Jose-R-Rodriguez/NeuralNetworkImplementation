import Connection
import Neuron as neuron
from NeuralNetwork import Network
def main():
	topology= []
	topology.append(2)
	topology.append(3)
	topology.append(3)
	topology.append(1)
	net= Network(topology)
	neuron.eta= 0.09
	neuron.alpha= 0.015
	inputs= [[0, 0],[0, 1],[1, 0],[1, 1]]
	outputs=[[0],[1],[1],[0]]
	while True:
		err= 0
		for i in range(len(inputs)):
			net.setInput(inputs[i])
			net.feedForward()
			net.backPropagate(outputs[i])
			err= err+ net.getError(outputs[i])
		print ("Error: ", err)
		if err < 1.5:
			break
	while True:
		a= int(input("First input: "))
		b= int(input("Second input: "))
		net.setInput([a, b])
		net.feedForward()
		print (net.getThResults())

if __name__ == '__main__':
	main()
