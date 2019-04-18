nums=int(input())
strs=[]
for i in range(nums):
	l=input()
	strs.append(input())

s_d={'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'Q':0,'K':0}

for s in strs:
	s_dd=[]
	s=s.split(' ')
	for si in s:
		s_d[si]+=1
	for key,value in s_d.items():
		s_dd.append(value)
	out=0
	for i in range(9):
		sumtemp = 1
		for j in range(i,i+5):
			sumtemp*=s_dd[j]
		out+=sumtemp
		j+=1
		while sumtemp and j<13:
			sumtemp*=s_dd[j]
			out+=sumtemp
			j+=1
	print(out)