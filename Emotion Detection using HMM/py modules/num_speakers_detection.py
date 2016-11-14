# Shouting and Non-shouting

from hmmlearn.hmm import GMMHMM
import numpy as np
import os
import pickle

#--------pre-processing to convert sequences in files into list of sequences---------#

def pre_process(fil):
	data = []
	data1=[]
	x=""
	for f in fil:
		if(not f==None):
			x=x+"\n"+open(f).read().strip()
	x.strip()
	data1=(x).split('\n')[1:]
	
	for fi in data1:		
		data.append(list(map(float,fi.split(','))))

	d = [np.array(map(np.array,data[i:i+200])) for i in range(0,len(data),200)]
	#print type(d),type(d[0]),type(d[0][0]),type(d[0][0][0]),len(d),len(d[0]),len(d[0][0])
	d =  np.array(d)
	#print type(d),type(d[0]),type(d[0][0]),type(d[0][0][0]),len(d),len(d[0]),len(d[0][0])
	return d

def test(fil):
	for f in fil:
		if(not f==None):
			dat=pre_process([f])
			# print f
			li=[]
			w = open(f+'.out3_3','w')
			for i in range(len(dat)):
				temp=[gmm[j].score(dat[i]) for j in range(2)]
				li.append(temp.index(max(temp)))
			w.write(str(li))

if __name__ == '__main__':

	gmm=[GMMHMM(n_components=3,n_mix=1,covariance_type='diag') for i in range(2)]

	path="./mfcc_files/"

	for p,subdirs,files in os.walk(path+"shouting"):    
		fp = files
	data_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))

	dat=pre_process(data_path)
	gmm[0].fit(dat)

	for p,subdirs,files in os.walk(path+"non_shouting"):    
		fp = files
	data_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))
	print dat
	dat=pre_process(data_path)
	gmm[1].fit(dat)

	k=[]

	pickle.dump(gmm[0],open('shouting.pickle','w'))
	pickle.dump(gmm[1],open('non_shouting.pickle','w'))
	
	path = './mfcc_files/Testing/'

	for p,subdirs,files in os.walk(path+"shouting"):    
		fp = files
	test_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))

	test(test_path)

	# for p,subdirs,files in os.walk(path+"non_shouting"):    
	# 	fp = files
	# test_path = list(map(lambda x: (p+"/"+x) if x.endswith(".txt") else None,fp))
	# test(test_path)
	
	# test_path = [path+'/host5_mfcc.txt']
	# test(test_path)
	# print k
	# count = 0
	# for i in range(len(k)):
	# 	for j in k[i]:
	# 		if i==j:
	# 			count += 1
				
	# print 'Accuracy : ',count/7.0*100






