import numpy as np
from network import Network
auto = Network([13,5,13])
#print auto.weights
lis=[]
f=open('./MFCC_Files/autoencoder_training_mfccs.txt').read().split('\n')
for i in f[:len(f)-2]:
	l=i.split(',')
	t1=[]
	tmp = [0.0]
	for y in l:
		#print y,type(y)
		try:
			tmp[0]=np.float32(float(y.strip()))
		except:
			print y
		#print tmp[0],type(eval(y))
		tmp=np.array(tmp)
		t1.append(tmp)
	lis.append((np.array(t1),(np.array(t1))))
print len(lis)
print type(lis[0][0][0][0])

auto.SGD(lis,1,1,0.00001)
def sigmoid(z): 	
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

sigmoid_vec = np.vectorize(sigmoid)

f=open('./MFCC_Files/c2_test_mfcc.txt').read().split('\n')
for i in f[:len(f)-2]:
	l=i.split(',')
	t1=[]
	tmp = [0.0]
	for y in l:
		#print y,type(y)
		try:
			tmp[0]=np.float32(float(y.strip()))
		except:
			print y
		#print tmp[0],type(eval(y))
		tmp=np.array(tmp)
		t1.append(tmp)
	lis.append((np.array(t1),(np.array(t1))))
print auto.weights
p = open("c2_test_mfcc_output.txt","w")
for i in range(len(f)-2):
	#print "out[",i,"]",auto.feedforward(batch[i][1])
	a=sigmoid_vec(np.dot(auto.weights[0],lis[i][0])+auto.biases[0])
	pq=[1 if x>0.5 else 0 for x in a]
	out=0
	for i in pq:
		out=2*out+i
	p.write(str(pq)+'-'+str(out)+'\n')

