import Connection
import threading
import Neuron as neuron
from NeuralNetwork import Network

def TrainNet(inputs1, net1, outputs1, id, result_list):
	while True:
		#print ("Training,", id)
		err= 0
		for i in range(len(inputs1)):
			net1[0].setInput(inputs1[i])
			net1[0].feedForward()
			net1[0].backPropagate(outputs1[i])
			err= err+ net1[0].getError(outputs1[i])
		print ("Error: ", err)
		if err < 0.6:
			print ("I have finished", id)
			result_list[id]= net1[0]
			break
def main():
	result_list= [[None], [None]]
	topology= []
	topology.append(2)
	topology.append(3)
	topology.append(3)
	topology.append(1)
	net1= Network(topology)
	net2= Network(topology)
	neuron.eta= 0.09
	neuron.alpha= 0.015
	inputs1= [[0, 0],[0, 1]]
	outputs1=[[0],[1]]
	inputs2= [[1, 0],[1, 1]]
	outputs2=[[1],[0]]
	threads= []
	nets= [net1, net2]
	outputs=[outputs1, outputs2]
	inputs= [inputs1, inputs2]
	for i in range(2):
		t= threading.Thread(target=TrainNet, args=(inputs[i], [nets[i]], outputs[i], i, result_list))
		threads.append(t)
		t.start()
	for i in range(2):
		threads[i].join()
	net1= result_list[0]
	net2= result_list[1]
	while True:
		a= int(input("First input: "))
		b= int(input("Second input: "))
		if (a>0):
			net2.setInput([a, b])
			net2.feedForward()
			print (net1.getThResults())
		else:
			net1.setInput([a, b])
			net1.feedForward()
			print (net1.getThResults())
if __name__ == '__main__':
	main()
