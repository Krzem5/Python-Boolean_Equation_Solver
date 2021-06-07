def alloc(n):
	return [None for _ in range(0,n)]



def __bsf(n):
	o=0
	while (not (n&1)):
		n>>=1
		o+=1
	return o



def __popcnt(n):
	o=0
	while (n):
		if (n&1):
			o+=1
		n>>=1
	return o



def __parity(n):
	o=0
	while (n):
		if (n&1):
			o^=1
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
			i=__popcnt(e)
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
	o=0
	om=mx
	sz=len(l)
	a=alloc(sz)
	na=alloc(sz)
	for i,k in enumerate(l):
		a[i]=0
		for e in k:
			a[i]|=1<<v.index(e)
		na[i]=a[i]
	while (True):
		i=0
		m=1
		for j in range(0,vl):
			k=i
			t=na[i]
			while (not (t&m)):
				k+=1
				if (k==len(a)):
					break
				t=na[k]
			if (t&m):
				na[k]=na[i]
				na[i]=t
				for k in range(i+1,sz):
					if (na[k]&m):
						na[k]^=na[i]^m
				i+=1
				if (i==len(a)):
					break
			m<<=1
		s=0
		m=b
		while (m):
			s^=na[__bsf(m)]
			m&=m-1
		if (vml==1):
			return o|(s&om)
		rm=True
		for k in vm[vml-1]:
			m=1<<v.index(k)
			if (s&m):
				om&=~k
				o|=k
				while (k):
					m|=1<<v.index(k&(-k))
					k&=k-1
				im=~m
				for i in range(0,sz):
					b^=__parity(a[i]&m)<<i
					a[i]&=im
			else:
				rm=False
				print("Unknown Combination")
		if (rm):
			vml-=1
			while (len(vm[vml])==0):
				vml-=1
		for i in range(0,sz):
			na[i]=a[i]



o=solve(0b01,[0b001,0b010,0b011],[0b001,0b010,0b100])
print(f"a^b^(a&b)=1, a^b^c=0 -> a={o&1}, b={(o>>1)&1}, c={o>>2}")

