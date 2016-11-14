from bs4 import BeautifulSoup
import re,csv

big_dict = {}
def write_comms():
	soup = BeautifulSoup(open("1.html").read(), 'html.parser')
	d = {}
	nodes = soup.find_all("div","commentary-event")
	extra_comms  = []
	table = []
	for node in nodes:
		try:
			ball = float(node.find_all("div","commentary-overs")[0].get_text())
			try:
				comm = str(node.find_all("div","commentary-text")[0].p.get_text())
				comm = re.sub(r'[\r\t]','',comm)
				d[ball] = comm
			except:
				pass
		except:
			pass
	big_dict["comments"] = d
	out = sorted(d.items(),key=lambda x:x[0])
	f = open("comms.txt","w")
	writer = csv.writer(open("Events_4_2.csv","w"))
	for s in out:
		l = []
		l.append(s[1])
		l.extend(['0']*22)
		writer.writerow(l)
		f.write(str(s[1])+"\n")

	bowlers = {}
	nodes = soup.find_all("ul","end-of-over-bowlers")
	for node in nodes:
		s = node.li.get_text().strip().split(" ")
		pl = " ".join(s[:-1])
		stat = s[-1]
		bowlers[pl] = stat
	big_dict["bowlers"] = bowlers

	outs = []
	nodes = soup.find_all("div","commentary-text")
	for node in nodes:
		try:
			line = node.p.b.get_text()
			line = re.sub(r'[\r\t]','',line)
			outs.append(str(line.strip()))
		except:
			pass
	big_dict["outs"] = outs

	open("Match_4_2.json","w").write(str(big_dict))


write_comms()