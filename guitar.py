
l = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
l1 = ["Am","A#m","Bm","Cm","C#m","Dm","D#m","Em","Fm","F#m","Gm","G#m"]
print("How many Choard?")
n = input()
n = int(n)
d  = []
i = 0

while i<n:
	f = input()
	d = d + [f]
	i = i +1 
print("====================")
def scale_up(choard,level):
	c = num(choard)
	if c>= 100:
		c = c- 100
		if c+level<12:
			q=  c+ level
		else:
			q= (c+level)-12
		return l1[q]
	else:
		if c+level<12:
			q=  c+ level
		else:
			q= (c+level)-12
		return l[q]

def num(choard):
	p=-1
	for t in l:
		p= p+1
		if t == choard:
			return p
			break
		
	
	p = 99
	for t in l1:
		p= p+1
		if t == choard:
			return p
			break
	
	

i=0
while(i<12):
	n = []
	for z in d:
		n = n + [scale_up(z,i)]
	i= i +1
	print(str(n))
input()

