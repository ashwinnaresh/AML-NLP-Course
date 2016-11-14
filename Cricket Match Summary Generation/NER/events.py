def f(l):
	p = dict()
	for t in l:
		if t[1] == "Batsman":
			params["Batsman"] = t[0]
		elif t[1] == "Bowler":
			params["Bowler"] = t[0]
		elif t[1] == "Fielder":
			params["Fielder"] = t[0]
		elif t[1] == "Fielding_Position":
			params["Fielding_Position"] == t[0]
		elif t[1] == "Non striker":
			params["Non striker"] = t[0]
	return p

def Defended(l,comment_str):
	d = dict()
	d["Event_type"] = "Defended"
	params = d(l)
	if "length" in comment_str:
		for i in range(len(comment_str.split(" ")) - 1):
			t = [comment_str[i],comment_str[i+1]]	
			flag = 1
			for j in t:
				if j[1] == "length":
					params["Ball_type"] = " ".join(t)
					flag = 1
			if flag == 0:
				params["Ball_type"] = "Unknown"
	d["Parameters"] = params
	return d

def Left_alone(l,comment_str):
	d = dict()
	d["Event_type"] = "Left_alone"
	params = f()
	d["Parameters"] = params
	return d

def Beaten(l,comment_str):
	d = dict()
	d["Event_type"] = "Beaten"
	params = f()
	for i in range(len(temp)):
		if temp[i] =="misses" or temp[i]=="missed" or temp[i]=="miss":
			params["missed_result"] = temp[i:]
	d["Parameters"] = params
	return d

def Edged(l,comment_str):
	d = dict()
	d["Event_type"] = "Edged"
	params = f()
	if "run" in comment_str or "runs" in comment_str:
		for t in l:
			if t[1] == "run" or t[1] == "runs":
				params["run_from_ball"] = t[0]
	temp = comment_str.split(" ")
	flag = 0
	for i in range(len(temp)):
		if temp[i] =="edge" or temp[i] == "edged":
			params["edged_result"] = temp[i:]
		if temp[i] == "OUT":
			params["OUT"] = "Yes"
			flag = 1
	if not flag:
		params["OUT"] = "False"
	d["Parameters"] = params
	return d

def Caught(l,comment_str):
	d = dict()
	d["Event_type"] = "Caught"
	params = f()
	d["Parameters"] = params
	return d

def Runout(l,comment_str):
	d = dict()
	d["Event_type"] = "Runout"
	params = f()
	if "run" in comment_str or "runs" in comment_str:
		for t in l:
			if t[1] == "run" or t[1] == "runs":
				params["run_from_ball"] = t[0]
	d["Parameters"] = params
	return d

def Stumped(l,comment_str):
	d = dict()
	d["Event_type"] = "Stumped"
	params = f()
	d["Parameters"] = params
	return d

def Bowled(l,comment_str):
	d = dict()
	d["Event_type"] = "Bowled"
	params = f()
	d["Parameters"] = params
	return d

def LBW(l,comment_str):
	d = dict()
	d["Event_type"] = "LBW"
	params = f()
	d["Parameters"] = params
	return d

def Boundary_scored_by_batsman(l,comment_str):
	d = dict()
	d["Event_type"] = "Boundary_scored_by_batsman"
	params = f()
	if "FOUR" in comment_str:
		params["type"] = "FOUR"
	else:
		params["type"] = "SIX"
	d["Parameters"] = params
	return d