f1 = eval(open('mfcc_files/Testing/shouting/arnab_8_mfcc.txt.out3_1').read().strip())
f2 = eval(open('mfcc_files/Testing/shouting/arnab_8_mfcc.txt.out3_2').read().strip())
f3 = eval(open('mfcc_files/Testing/shouting/arnab_8_mfcc.txt.out3_3').read().strip())

d = {0:0,1:0,2:0}
count = 0

for i in range(len(f1)):
	if f1[i] == 0:
		if f2[i] == 0:
			if f3[i] == 0:
				d[0] += 1

		if f2[i] == 1:
			if f3[i] == 0:
				d[1] += 1

		if f2[i] == 2:
			if f3[i] == 0:
				d[2] += 1

print d


