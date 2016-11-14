import numpy as np
from network import Network
auto = Network([8,3,8])
#print auto.weights
batch = [(np.array([np.array([[0.]]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.])]),np.array([np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.])])),
(np.array([np.array([[0.]]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.])]),np.array([np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.])])),
(np.array([np.array([[0.]]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.])]),np.array([np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.])])),
(np.array([np.array([[0.]]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.])]),np.array([np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.])])),
(np.array([np.array([[0.]]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])]),np.array([np.array([0.]),np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])])),
(np.array([np.array([[0.]]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])]),np.array([np.array([0.]),np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])])),
(np.array([np.array([[0.]]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])]),np.array([np.array([0.]),np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])])),
(np.array([np.array([[1.]]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])]),np.array([np.array([1.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.]),np.array([0.])]))
]

#np.array([np.float32(0),np.float32(0),np.float32(0),np.float32(0),np.float32(0),np.float32(0),np.float32(0),np.float32(1)]
print type(batch[0][0][0])
auto.SGD(batch,1,1,0.00001)
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

sigmoid_vec = np.vectorize(sigmoid)
print auto.weights
for i in range(8):
	#print "out[",i,"]",auto.feedforward(batch[i][1])
	a=sigmoid_vec(np.dot(auto.weights[0],batch[i][0])+auto.biases[0])
	print "out[",i,"]",[1 if x>0.5 else 0 for x in a]

