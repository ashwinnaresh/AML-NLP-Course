from nltk.tokenize import *
import csv

word_tags = []
batsmen = []
bowlers_fielders = []
runs = ["FOUR","SIX"]
d = eval(open("positions.txt").read())
fielding_pos = map(str.lower,[v for k in d.keys() for v in d[k]])

def tokenizer(f):
	lines = open(f).read()
	sents = lines.split("\n")[:75]
	for sent in sents:
		parts = sent.split(",")
		if "to" in parts[0]:
			bowler = parts[0].split("to")[0].strip()
			batsman = parts[0].split("to")[1].strip()
			batsmen.append(batsman)
			bowlers_fielders.append(bowler)
			word_tags.append(bowler+",BOWLER")
			word_tags.append("to,OTHER")
			word_tags.append(batsman+",BATSMAN")
		else:
			word_tags.extend([w+",OTHER" for w in parts[0].split(" ")])
		# for j in range(len(parts)):
		# 	word_tags.append(",,OTHER")
		words = " ".join(parts[1:]).split(" ")
		
		temp_fields = [p.split(" ") for p in fielding_pos]
		
		i = 0
		l = len(words)-1
		while i < l:
			t = [words[i],words[i+1]]

			if t in temp_fields:
				word_tags.append(" ".join(t)+",FIELDINGPOSITION")
				del words[i]
				del words[i+1]
				l = l-2
			else:
				i += 2
		
		for word in words:
			if len(word) > 0:
				# if word in fielding_pos:
				# 	word_tags.append(word+",FIELDINGPOSITION")
				if ord(list(word)[0]) >= 65 and ord(list(word)[0]) <= 90 and word not in runs:
					if  word != batsman:
						word_tags.append(word+",FIELDER")
						bowlers_fielders.append(word)
					elif (word in batsmen and word != batsman) or (word not in bowlers_fielders):
						word_tags.append(word+",NONSTRIKER")
				else:
					word_tags.append(word+",OTHER")
	open("tags.csv","w").write("\n".join(word_tags))

tokenizer("comms.txt")