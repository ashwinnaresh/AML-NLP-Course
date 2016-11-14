import math,re
from score import *
import random
comment_ds = dict()
target = 0
def find_event(comm_event,comm_tags,comm_str,ball_num,innings):
	#comment_str = " ".join([t[0] for t in comm])
	#print comment_str
	global target
	global chased
	global comment_ds
	event_ds = []
	for i in range(len(comm_event)):
		if comm_event[i] == 1:
			d=event_list[i](comm_tags,comm_str)
			d['Ball'] = (ball_num - math.floor(ball_num))
			d['Over'] = int(math.floor(ball_num))
			if(innings == 1):
				if(d['Over']<=10):
					d['Impact'] = 'High'
					d['Reason'] = 'Early in the innings. Top batsman not out'
				elif(d['Over']>=45):
					d['Impact'] = 'High'
					d['Reason'] = 'Needs more wickets'
				else:
					d['Impact'] = 'Low'
					d['Reason'] = 'Middle of match. Outcome can change'
				d['Score'] = target[ball_num]
			else:
				if(d['Over']<=10 and target[max(target.keys())]<250):
					d['Impact'] = 'High'
					d['Reason'] = 'Low score to chase. Missed out wickets'
				elif(d['Over']>=45 and target[max(target.keys())]-chase[ball_num]<=40):
					d['Impact'] = 'High'
					d['Reason'] = 'Needs more wickets'
				else:
					d['Impact'] = 'Low'
					d['Reason'] = 'Middle of match. Outcome can change'
				d['Score'] = chased[ball_num]

 	comment_ds[innings][ball_num] = d

def Catch_dropped(comm,comment_str):
	ev =  {"event_type":"Catch_dropped"}
	event_ds =  {"batsman":comment_str.split(",")[0].split("to")[1],"bowler":comment_str.split(",")[0].split("to")[1],"fielder":'',"fielding_postition":'',"non-striker":''}
	for tagged in comm:
		if(tagged[1]=="batsman"):
			event_ds["batsman"] =  tagged[0]
		elif(tagged[1]=="bowler"):
			event_ds["bowler"] = tagged[0]
		elif(tagged[1]=="fielder"):
			event_ds["fielder"] = tagged[0]
		elif(tagged[1]=="fielding_postition"):
			event_ds["fielding_postition"] = tagged[0]
		elif(tagged[1] == "non-striker"):
			event_ds["non-striker"] = tagged[0]
	try:
		if("FOUR" in comment_str or "4" in comment_str):
			runs = 4
		elif("SIX" in comment_str or "6" in comment_str):
			runs = 6
		elif ("1" in comment_str):
			runs = 1
		elif ("2" in comment_str):
			runs = 2
		elif ("3" in comment_str):
			runs = 3
		if("no run" in comment_str):
			runs = 0
	except:
		runs = "Unknown"
	event_ds["Runs"] = runs
	l = ['deep square','long-on','covers','square-leg','back to bowler','midwicket','backward square leg','bowler','back to the bowler','man in the deep','extra cover','deep square']
	for i in l:
		if i in comment_str:
			event_ds['fielder_position'] = i	
			break
	ev["parameters"] = event_ds
	return ev

def Runout_missed(comm,comment_str):
	ev =  {"event_type":"Runout_missed"}
	event_ds =  {"batsman":comment_str.split(",")[0].split("to")[1],"bowler":comment_str.split(",")[0].split("to")[1],"fielder":'',"fielding_postition":'',"non-striker":''}
	for tagged in comm:
		if(tagged[1]=="batsman"):
			event_ds["batsman"] =  tagged[0]
		elif(tagged[1]=="bowler"):
			event_ds["bowler"] = tagged[0]
		elif(tagged[1]=="fielder"):
			event_ds["fielder"] = tagged[0]
		elif(tagged[1]=="fielding_postition"):
			event_ds["fielding_postition"] = tagged[0]
		elif(tagged[1] == "non-striker"):
			event_ds["non-striker"] = tagged[0]
	try:
		if("FOUR" in comment_str or "4" in comment_str):
			runs = 4
		elif("SIX" in comment_str or "6" in comment_str):
			runs = 6
		elif ("1" in comment_str):
			runs = 1
		elif ("2" in comment_str):
			runs = 2
		elif ("3" in comment_str):
			runs = 3
		if("no run" in comment_str):
			runs = 0
	except:
		runs = "Unknown"
	event_ds["Runs"] = runs
	l = ['deep square','long-on','covers','square-leg','back to bowler','midwicket','backward square leg','bowler','back to the bowler','man in the deep','extra cover','deep square','cover','covers','deep','square-leg','mid-off','behind square','mid-on','off side','mid on']
	for i in l:
		if i in comment_str:
			event_ds['fielder_position'] = i	
			break
	ev["parameters"] = event_ds
	return ev

def Stumping_missed(comm,comment_str):
	ev =  {"event_type":"Stumping_missed"}
	event_ds =  {"batsman":comment_str.split(",")[0].split("to")[1],"bowler":comment_str.split(",")[0].split("to")[1],"fielder":'',"fielding_postition":'',"non-striker":''}
	for tagged in comm:
		if(tagged[1]=="batsman"):
			event_ds["batsman"] =  tagged[0]
		elif(tagged[1]=="bowler"):
			event_ds["bowler"] = tagged[0]
		elif(tagged[1]=="fielder"):
			event_ds["fielder"] = tagged[0]
		elif(tagged[1]=="fielding_postition"):
			event_ds["fielding_postition"] = tagged[0]
		elif(tagged[1] == "non-striker"):
			event_ds["non-striker"] = tagged[0]
	try:
		if("FOUR" in comment_str or "4" in comment_str):
			runs = 4
		elif("SIX" in comment_str or "6" in comment_str):
			runs = 6
		elif ("1" in comment_str):
			runs = 1
		elif ("2" in comment_str):
			runs = 2
		elif ("3" in comment_str):
			runs = 3
		if("no run" in comment_str):
			runs = 0
	except:
		runs = "Unknown"
	event_ds["Runs"] = runs
	l = ['deep square','long-on','covers','square-leg','back to bowler','midwicket','backward square leg','bowler','back to the bowler','man in the deep','extra cover','deep square','cover','covers','deep','square-leg','mid-off','behind square','mid-on','off side','mid on']
	for i in l:
		if i in comment_str:
			event_ds['fielder_position'] = i	
			break
	ev["parameters"] = event_ds
	return ev

def main():
	event_list = [Catch_dropped, Stumping_missed, Runout_missed]#,great_save,poor_fielding,Free_hit]
	comment_event = dict()
	target = calc_runs(1)
	chased = calc_runs(2)
	for j in range(1,3):
		events_vec =  eval(open("maxent_out"+str(j)+".txt","r").read())
		comments = eval(open("Match_4_"+str(j)+".json","r").read())['comments']
		tagged_comms = eval(open("ner_output"+str(j)+".txt","r").read())
		for i in events_vec.keys():
			l = events_vec[i]
			vec = [l[1],l[13],l[14],l[15]]
			find_event(vec,tagged_comms[i],comments[i],i,j)

	open("events.json","w").write(str(comment_ds))
	#find_event([0,0,0,0,1,0,0,0],[('Kumar','bowler'),('to','other'),('Amla','batsman'),('1','other'),('run','other'),("Amla's",'batsman'),('bat','other'),('comes','other'),('down','other'),('late','other'),('for','other'),('the','other'),('incoming','other'),('delivery','other'),('and','other'),('the','other'),('edge','other'),('goes','other'),('near','other'),('the','other'),('stumps','other'),('and','other'),('behind','other'),('square','fielding_postition'),('on','other'),('the','other'),('leg','other'),('side','other')])
	#find_event([0,0,0,1,1,0,0,0],[('Anwar','bowler'),('Ali','bowler'),('to','other'),('Root','batsman'),('FOUR','other'),('dropped','other'),('short','other'),('by','other'),('Anwar','bowler'),('and','other'),('Root','batsman'),('thwocks','other'),('a','other'),('pull','other'),('away','other'),('to','other'),('the','other'),('square','fielding_postition'),('leg,fielding_postition'),('boundary','other'),('with','other'),('control','other'),('to','other'),('spare','other')],"0.5")


def describe_missed_catches():
	d_1= eval(open("events.json","r").read())[1]
	d_2 = eval(open("events.json","r").read())[2]
	for balls in d_1.keys():
		for ev in balls:
			if(ev['event_type'] == 'Runout_missed'):
				runout_template(ev)
			if(ev['event_type'] == 'Stumping_missed'):
				stumping_template(ev)
			if(ev['event_type'] == 'Catch_dropped'):
				catch_template(ev)

def catch_template(ev):
	batsman = ev['parameters']['batsman']
	bowler = ev['parameters']['bowler']
	fielder = ev['parameters']['fielder']
	fielder_position = ev['parameters']['fielder_position']
	score = str(ev['Score'])
	runs = str(ev['parameters']['Runs'])
	impact = ev['Impact']
	reason = ev['Reason']
	ball = str(ev['Ball'])
	over = str(ev['Over'])
	s1 = "In the over "+over+", "+batsman+" was dropped at "+fielder_position+" when the score was "+ score+" and the bowler involved was "+bowler+"."
	s1+="The impact was "+impact+"."+"The reason for such an impact is "+reason+"."
	s2 = "The catch was dropped in over number "+over+" when the batsman involved was "+batsman+". He scored "+runs+" runs pushing the score to "+score+"."
	s2+="This had a "+impact+" impact on the match."
	import random
	r = random.randint(0,1)
	if(r == 1):
		print s1
	else:
		print s2

def runout_template(ev):
	batsman = ev['parameters']['batsman']
	bowler = ev['parameters']['bowler']
	fielder = ev['parameters']['fielder']
	fielder_position = ev['parameters']['fielder_position']
	score = str(ev['Score'])
	runs = str(ev['parameters']['Runs'])
	impact = ev['Impact']
	reason = ev['Reason']
	ball = str(ev['Ball'])
	over = str(ev['Over'])
	s1 = "In the over "+over+", "+batsman+" had a missed runout when the score was "+ score+" and the bowler involved was "+bowler+"."
	s1+="The impact was "+impact+"."+"The reason for such an impact is "+reason+"."
	s2 = "An attempt at a run out was missed in over number "+over+" when the batsman involved was "+batsman+". He scored "+runs+" runs pushing the score to "+score+"."
	s2+="This had a "+impact+" impact on the match."
	r = random.randint(0,1)
	if(r == 1):
		print s1
	else:
		print s2

def stumping_template(ev):
	batsman = ev['parameters']['batsman']
	bowler = ev['parameters']['bowler']
	fielder = ev['parameters']['fielder']
	fielder_position = ev['parameters']['fielder_position']
	score = str(ev['Score'])
	runs = str(ev['parameters']['Runs'])
	impact = ev['Impact']
	reason = ev['Reason']
	ball = str(ev['Ball'])
	over = str(ev['Over'])
	s1 = "In the over "+over+", "+" missed an opportunity for stumping of "+batsman+" when the score was "+ score+" and "+bowler+" was bowling."
	s1+="The impact was "+impact+"."+"The reason for such an impact is "+reason+"."
	s2 = "An attempt at a stumping was missed in over number "+over+" when the batsman was "+batsman+". He scored "+runs+" making the score "+score+"."
	s2+="This had a "+impact+" impact on the match."
	r = random.randint(0,1)
	if(r == 1):
		print s1
	else:
		print s2

js = eval(open("events.json","r").read())
catch_template(js[0])
runout_template(js[1])