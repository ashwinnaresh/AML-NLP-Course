import re,nltk,csv
from nltk import word_tokenize
from my_maxent_test import MyMaxEnt
import numpy as np
import feature_functions as f 

if __name__ == '__main__':
	r = open('data.csv','rb')
	targets = []
	inputs = []
	tags = ['Defended','Left alone','Beaten','Edged','Caught','Runout','Stumped','Bowled','LBW','Boundary_scored_by_batsman','Runs_by_batsman','Boundary_scored_extras','Runs_by_extras','Catch_dropped','Stumping Missed','Runout Missed','Bouncer','Yorker','Overthrow','great_save','poor_fielding','Free hit']
	funcs = [f.f1,f.f2,f.f3,f.f4,f.f5,f.f6,f.f7,f.f8,f.f9,f.f10,f.f11,f.f12,f.f13,f.f14,f.f15,f.f16,f.f17,f.f18,f.f19,f.f20,f.f21,f.f22]
	reader = csv.reader(r)
	i = 0
	for row in reader:
		i += 1
		if i == 1 or i == 2:
			continue
		else:
			# print i
			comment = tuple(word_tokenize(row[1]))
			inputs.append([comment,list(map(lambda x:0 if x == '' else int(x),row[2:]))])

	# create multiple max ent classifers and save their models
	# Training
	out = zip(*inputs)[1]
	out1 = zip(*inputs)[0]
	out_vec = [i[0:3] for i in out]
	inp = zip(out1,out_vec)
	c1 = MyMaxEnt(inp,[f.f1,f.f2,f.f3],['Defended','Left alone','Beaten'])
	c1.train()
	c1.save('c1_model.pickle')
	# print c1.classify(inp[0][0])
	# print inp[0][1]

	out_vec = [[i[4],i[6],i[7],i[8],i[13],i[14],i[15],i[21]] for i in out]
	inp = zip(out1,out_vec)
	c2 = MyMaxEnt(inp,[f.f5,f.f7,f.f8,f.f9,f.f14,f.f15,f.f16,f.f22],['Caught','Stumped','Bowled','LBW','Catch_dropped','Stumping Missed','Runout Missed','Free hit'])
	c2.train()
	c2.save('c2_model.pickle')

	out_vec = [[i[5],i[7],i[9],i[10],i[11],i[12]]for i in out]
	inp = zip(out1,out_vec)
	c3 = MyMaxEnt(inp,[f.f6,f.f8,f.f10,f.f11,f.f12,f.f13],['Runout','Bowled','Boundary_scored_by_batsman','Runs_by_batsman','Boundary_scored_extras','Runs_by_extras'])
	c3.train()
	c3.save('c3_model.pickle')

	out_vec = [[i[16],i[17]]for i in out]
	inp = zip(out1,out_vec)
	c4 = MyMaxEnt(inp,[f.f17,f.f18],['Bouncer','Yorker'])
	c4.train()
	c4.save('c4_model.pickle')

	out_vec = [[i[19],i[20]]for i in out]
	inp = zip(out1,out_vec)
	c5 = MyMaxEnt(inp,[f.f20,f.f21],['great_save','poor_fielding'])
	c5.train()
	c5.save('c5_model.pickle')

	out_vec = [[i[3],i[18]]for i in out]
	inp = zip(out1,out_vec)
	c6 = MyMaxEnt(inp,[f.f4,f.f19],['Edged','Overthrow'])
	c6.train()
	c6.save('c6_model.pickle')

	'''
	c1 = MyMaxEnt(inputs,funcs,[1 if tags[i] in ['Defended','Left alone','Beaten'] else 0 for i in range(len(tags))])
	c1 = c1.load('c1_model.pickle')
	c2 = MyMaxEnt(inputs,funcs,[1 if tags[i] in ['Caught','Catch_dropped','LBW','Stumping Missed','Bowled','Free hit','Runout Missed','Stumped'] else 0 for i in range(len(tags))])
	c2 = c2.load('c2_model.pickle')
	c3 = MyMaxEnt(inputs,funcs,[1 if tags[i] in ['Runs_by_batsman','Runs_by_extras','Boundary_scored_by_batsman','Boundary_scored_extras','Runout','Bowled'] else 0 for i in range(len(tags))])
	c3 = c3.load('c3_model.pickle')
	c4 = MyMaxEnt(inputs,funcs,[1 if tags[i] in ['Bouncer','Yorker'] else 0 for i in range(len(tags))])
	c4 = c4.load('c4_model.pickle')
	c5 = MyMaxEnt(inputs,funcs,[1 if tags[i] in ['great_save','poor_fielding'] else 0 for i in range(len(tags))])
	c5 = c5.load('c5_model.pickle')
	c6 = MyMaxEnt(inputs,funcs,[1 if tags[i] in ['Overthrow','Edged'] else 0 for i in range(len(tags))])
	c6 = c6.load('c6_model.pickle')

	classifiers = [c1,c2,c3,c4,c5,c6]
	count = 0
	test_data = inputs[3000:]
	# for data in test_data:
	# 	tot_out = [0]*22
	# 	for c in classifiers:
	# 		out_t = c.classify(data[0])
	# 		if out_t != 'OTHER':
	# 			tot_out[tags.index(out_t)] = 1
	# 	if tot_out == data[1]:
	# 		count += 1
			# print count
	temp = []
	temp2 = []
	for data in test_data:
		tot_out = [0]*22
		for c in classifiers:
			out_t = c.classify(data[0])
			if out_t != 'OTHER':
				tot_out[tags.index(out_t)] = 1
		temp.extend(tot_out)
		temp2.extend(data[1])
	for i in range(len(temp)):
		if temp[i] == temp2[i]:
			count += 1

	print count,count/float(len(temp))
	# print len(test_data)
	'''
	# Testing
	out_vec = [i[0:3] for i in out]
	inp = zip(out1,out_vec)
	c1 = MyMaxEnt(inp,[f.f1,f.f2,f.f3],['Defended','Left alone','Beaten'])
	out_vec = [[i[4],i[6],i[7],i[8],i[13],i[14],i[15],i[21]] for i in out]
	inp = zip(out1,out_vec)
	c2 = MyMaxEnt(inp,[f.f5,f.f7,f.f8,f.f9,f.f14,f.f15,f.f16,f.f22],['Caught','Stumped','Bowled','LBW','Catch_dropped','Stumping Missed','Runout Missed','Free hit'])	
	out_vec = [[i[5],i[7],i[9],i[10],i[11],i[12]]for i in out]
	inp = zip(out1,out_vec)
	c3 = MyMaxEnt(inp,[f.f6,f.f8,f.f10,f.f11,f.f12,f.f13],['Runout','Bowled','Boundary_scored_by_batsman','Runs_by_batsman','Boundary_scored_extras','Runs_by_extras'])	
	out_vec = [[i[16],i[17]]for i in out]
	inp = zip(out1,out_vec)
	c4 = MyMaxEnt(inp,[f.f17,f.f18],['Bouncer','Yorker'])
	out_vec = [[i[19],i[20]]for i in out]
	inp = zip(out1,out_vec)
	c5 = MyMaxEnt(inp,[f.f20,f.f21],['great_save','poor_fielding'])
	out_vec = [[i[3],i[18]]for i in out]
	inp = zip(out1,out_vec)
	c6 = MyMaxEnt(inp,[f.f4,f.f19],['Edged','Overthrow'])

	c1 = c1.load('c1_model.pickle')
	c2 = c2.load('c2_model.pickle')
	c3 = c3.load('c3_model.pickle')
	c4 = c4.load('c4_model.pickle')
	c5 = c5.load('c5_model.pickle')
	c6 = c6.load('c6_model.pickle')

	classifiers = [c1,c2,c3,c4,c5,c6]
	
	test_data = out1
	temp = []
	# for data in test_data:
		# tot_out = [0]*22
		# for c in classifiers:
		# 	out_t = c.classify(data)
		# 	if out_t != 'OTHER':
		# 		tot_out[tags.index(out_t)] = 1
		# temp.append(tot_out)

	# testing = out[3000:]
	# count = 0
	# print len(temp),len(testing)
	# for i in range(len(temp)):
	# 	if temp[i] == testing[i]:
	# 		count += 1
	# print count/float(len(testing))
	
	k = 1
	for c in classifiers:
		count = 0
		tot_out = [0]*len(c.feature_fn_list)
		for i in range(len(test_data)):
			t = c.classify(test_data[i])
			ll = [1 if not t == 'OTHER' and j == c.tags.index(t) else 0 for j in range(len(c.tags))]
			if ll == c.correct_tags[i]:
				count += 1

		print 'Classifier : ',k
		print 'Accuracy : ',count/float(len(test_data))*100
		k += 1

	for data in test_data:
		tot_out = [0]*22
		for c in classifiers:
			out_t = c.classify(data)
			if out_t != 'OTHER':
				tot_out[tags.index(out_t)] = 1
		temp.append(tot_out)

	count = 0
	# print len(temp),len(testing)
	# for i in range(len(temp)):
	# 	if temp[i] == out[i]:
	# 		count += 1
	# print 'Final : ', count/float(len(temp))*100
	
	'''
	p=0
	for data in test_data:
		tot_out = [0]*22
		out_t = c1.classify(data)
		if out_t != 'OTHER':
			# print out_t
			tot_out[tags.index(out_t)] = 1
			if out_t == 'Defended' or out_t == 'Beaten' or out_t == 'Left alone':
				print tot_out, out[out1.index(data)]
				p+=1
	print p,len(test_data)
	'''
	
	matches = eval(open('Match_13_2.json').read())
	d = {}
	for match in matches['comments'].items():
		tot_out = [0]*22
		for c in classifiers:
			comment = tuple(word_tokenize(match[1]))
			# print comment
			out_t = c.classify(comment)
			if out_t != 'OTHER':
				tot_out[tags.index(out_t)] = 1
		d[match[0]] = tot_out

	open('maxent_out_13_2.txt','w').write(str(d))
	