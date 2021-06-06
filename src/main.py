def bsf(n):
	o=0
	while (not (n&1)):
		n>>=1
		o+=1
	return o



def bsr(n):
	o=63
	m=0x8000000000000000
	while (not (n&m)):
		m>>=1
		o-=1
	return o




def popcnt(n):
	o=0
	while (n):
		if (n&1):
			o+=1
		n>>=1
	return o



def solve(b,*l):
	vl=0
	mx=0
	v=[]
	vl=0
	vm=[]
	vml=0
	for k in l:
		for e in k:
			if (e not in v):
				v.append(e)
				vl+=1
			i=popcnt(e)
			if (i>vl):
				vl=i
			while (vml<i):
				vm.append([])
				vml+=1
			if (e not in vm[i-1]):
				vm[i-1].append(e)
			mx|=e
	if (mx&(mx+1)):
		raise RuntimeError("Not All Identifiers Used")
	mx_sz=bsr(mx)+1
	o=0
	om=mx
	a=[0 for _ in range(0,len(b))]
	for i,k in enumerate(l):
		for e in k:
			a[i]|=1<<v.index(e)
	while (True):
		na=a[:]
		i=0
		for j in range(0,vl):
			mx=i
			mx_v=na[i]&(1<<j)
			while (mx_v==0):
				mx+=1
				if (mx==len(a)):
					break
				mx_v=na[mx]&(1<<j)
			if (mx_v!=0):
				t=na[mx]
				na[mx]=na[i]
				na[i]=t
				for k in range(i+1,len(a)):
					if (na[k]&(1<<j)):
						na[k]=(na[k]&(~(1<<j)))^na[i]
				i+=1
				if (i==len(a)):
					break
		s=0
		for i in range(0,len(a)):
			for j in range(0,vl):
				s^=(b[i]&(na[i]>>j))<<j
		if (vml==1):
			return o|(s&om)
		vml-=1
		for k in vm[vml]:
			m=1<<v.index(k)
			if (s&m):
				for i in range(0,len(a)):
					if (a[i]&m):
						a[i]&=~m
						b[i]^=1
				while (k):
					i=1<<bsf(k)
					k&=~i
					om&=~i
					o|=i
					m=1<<v.index(i)
					for j in range(0,len(a)):
						if (a[j]&m):
							a[j]&=~m
							b[j]^=1
			else:
				print("Unknown Combination")
		while (len(vm[vml])==0):
			vml-=1



o=solve([1,0],[1,2,3],[1,2,4])
print(f"a^b^(a&b)=1, a^b^c=0 -> a={o&1}, b={(o>>1)&1}, c={o>>2}")

