import numpy as np
from scipy.optimize import minimize as mymin 
import pickle, math

class MyMaxEnt(object):
	'''
		Python Class for the Maximum Entropy Classifier
	'''
	def __init__(self, hist_list, feature_fn_list, tags):
		'''
			Initialises the Max Ent model by producing the feature vectors for the training data
		'''
		self.hist_list = zip(*hist_list)[0]
		# print type(self.hist_list)
		self.correct_tags = zip(*hist_list)[1]
		# print type(self.correct_tags)
		self.tags = tags
		# self.and_vec = and_vec
		self.feature_fn_list = feature_fn_list
		self.fvectors, self.training_examples = self.create_dataset(feature_fn_list)
		# print len(self.fvectors.keys()),len(self.training_examples.keys())
		self.init_model()  # initialise the model
		
		s = np.array([0]*len(self.feature_fn_list))
		# temp = []
		# temp = [self.fvectors[j][j[4]] for j in self.fvectors.keys()]
		# print temp[0]
		# for i in temp:
		# 	s = np.add(s,np.array(i))
		# self.cum_f = s
		# print self.cum_f.size
		# cou = 0
		# for i in range(len(self.training_examples.values())):
		# 	if not type(self.training_examples.values()[i]) == list:
		# 		cou += 1
				# print self.training_examples.keys()[i],cou

	def init_model(self):
		'''
			Initialises the model parameter
		'''
		self.model = np.array([0.]*(len(self.feature_fn_list)))

	def getTag(self,t):
		'''
			Returns tag corresponding to the event
		'''
		if 1 in t:
			return self.tags[t.index(1)]
		else:
			return 'NO EVENT'

	def cost(self,model):
		'''
			Given the model, compute the cost 
		'''
		# we need to return negative of cost
		# self.model = model		
		self.count+=1
		L_of_v = 0.

		for i in self.fvectors.keys():
			# print self.training_examples[i]
			t = self.getTag(self.training_examples[i])
			if t != 'NO EVENT':
				L_of_v += math.log(self.p_y_given_x(i,t,model))
			else:
				L_of_v += math.log(1/float(len(self.feature_fn_list)))
		return -L_of_v

	def train(self):
		'''
			Train the classifier
		'''
		self.count = 0
		# params = mymin(self.cost, self.model, method = 'L-BFGS-B', jac = self.gradient, options = {'disp' : True})
		params = mymin(self.cost, self.model, method = 'L-BFGS-B', options = {'disp' : True})
		self.model = params.x
		# help(params)
		print "Done Training", self.model, self.count, params.success

	def p_y_given_x(self,h,tag,x):
		'''
			Take the history tuple and the required tag as the input and return the probability
		'''
		# print type(h),type(tag),type(x)
		return float(math.exp(np.dot(x,self.fvectors[h][tag])))/sum([math.exp(np.dot(x,self.fvectors[h][t])) for t in self.tags])

	def classify(self,h):
		'''
			Performs the classification by determining the tag that maximizes the probability
		'''
		max_prob = 0
		best_tag = ""
		self.fvectors[h] = {}
		for tag in self.tags:
			self.fvectors[h][tag] = [fun(h,tag) for fun in self.feature_fn_list]
		for tag in self.tags:
			prob = self.p_y_given_x(h,tag,self.model)
			if prob > max_prob:
				max_prob = prob
				best_tag = tag

			if max_prob == 1/float(len(self.feature_fn_list)):
				best_tag = "OTHER"
				
		return best_tag

	def gradient(self, x):
		'''
			Maximizes the log-likelihood(Minimizes the negative)
		'''
		# self.model = x
		print "self.model=",self.model
		temp = np.array([0]*len(self.feature_fn_list))
		for h in self.fvectors.keys():
			for tag in self.tags:
				# print self.p_y_given_x(h, tag),self.fvectors[h][tag] * self.p_y_given_x(h, tag)
				# import time 
				# time.sleep(5)
				temp = np.add(temp, (self.fvectors[h][tag] * self.p_y_given_x(h, tag, x)))
		# print "temp=",temp
		# derivative = np.add(self.cum_f, np.negative(temp))
		derivative = np.add(temp, np.negative(self.cum_f))
		print "derivative=",derivative
		return derivative
		
	def create_dataset(self, feature_fn_list):
		dataset1 = {k:{} for k in self.hist_list}
		for i in self.hist_list:
			for tag in self.tags:
				# print [fun(i,tag) for fun in feature_fn_list]
				dataset1[i][tag] = [fun(i,tag) for fun in feature_fn_list]
		
		dataset = {k:{} for k in self.hist_list}
		for i in range(len(self.hist_list)):
			dataset[self.hist_list[i]] = self.correct_tags[i]
		
		return dataset1, dataset
		
	def load(self,model_file):
		'''
			Load the Max Ent model from the model file
		'''
		return pickle.load(open(model_file))

	def save(self,model_file):
		'''
			Save the model 
		'''
		pickle.dump(self,open((model_file),"w"))
