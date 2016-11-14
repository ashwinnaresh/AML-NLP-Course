import neurolab as nl
import numpy as np
#from matplotlib import pylab as pl
from ocr import * 

flag=0
print 'expected obtained'
def train(inp,target,flag):
	#net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5]], [5, 1])
	global net
	net = nl.net.newff([[0, 1]] *128, [32, 26])		#128 input nodes,16 hidden nodes,26 output nodes
	if flag ==1:net.layers[-1].transf = nl.trans.LogSig()	#if flag is 1,output layer transfer function is Logistic Regression
	else:net.layers[-1].transf = nl.trans.SoftMax()		#if 0,SoftMax CLassifier is used
	err = net.train(inp, target, show=1,epochs=65)	#Gradient Descent Backpropagation	
	
	net.save('netTrained64_.txt')

def test(test_input):
	#net=nl.load('netTrained16_.txt')
	#print type(test_input)	
	count = 0
	c=0
	#print (test_input['a'][904])
	#print(test_input.values()[0])
	for k,v in test_input.items():
		#print v
		for key,val in v.items():
			print k,
			test_arr=net.sim([val])				#testing	
			#print 'in test',test_arr
			#time.sleep(3)
			base=ord('a') #ascii value of a				
			test_arr=test_arr.tolist()
		# for l in test_arr:
			identified_char=base+test_arr[0].index(max(test_arr[0]))	#the ascii value of the identified character
			print chr(identified_char)
			if chr(identified_char) == k:
				count += 1
			c+=1
	print 'accuracy : ' ,count/200.*100,'count',count
	#print the identified character
	#print test_arr.index(max(test_arr))

#test(inp[3])

if __name__ == '__main__':
	#neuralData=neuralPreprocess()
	target=[]
	filename = 'letter.data'
	f=open(filename)
	s=f.read().strip()
	inp=s.split('\n')[:800]
	test_temp=s.split('\n')[800:1000]
	out=[]
	'''for i in inp:
		temp=i.split()
		#print temp
		out[temp[1]]={}'''
	for i in inp:
		temp=i.split()
		out.append(list(map(float,temp[6:])))
		target.append([1. if chr(x+97)==temp[1] else 0. for x in range(26)])
		#print len(out[temp[1]][int(temp[0])])
	test_data ={}
	for i in test_temp:
		temp=i.split()
		#print temp
		test_data[temp[1]]={}
	for i in test_temp:
		temp=i.split()
		test_data[temp[1]][int(temp[0])]=list(map(float,temp[6:]))

	f.close()
	'''inp = out.values()
	print inp'''
	train(out,target,0)
	
	
	'''
	for i in range(26):
		for j in neuralData[chr(i+97)].keys()[:50]:
			inp.append(neuralData[chr(i+97)][j])
			target.append([1. if x==i else 0. for x in range(26)])
	
	print target
	train(inp,target,0)
	
	test_data=[]
	test_out=[]
	for i in range(26):
		for j in neuralData[chr(i+97)].keys()[50:60]:
			test_data.append(neuralData[chr(i+97)][j])
			test_out.append(chr(i+97))
			print chr(i+97)
	'''
	test(test_data)
	#print (neuralData['b'])
	


