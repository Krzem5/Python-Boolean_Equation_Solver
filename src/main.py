def alloc(n):
	return [None for _ in range(0,n)]



def realloc(a,l):
	if (a is None):
		return alloc(l)
	while (len(a)<l):
		a.append(None)
	return a



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



def solve(A,b):
	w=len(A)
	h=len(A[0])
	mx=0
	mx_sz=0
	vi=None
	vil=0
	for i in range(0,w):
		for j in range(0,h):
			e=A[i][j]
			if (not (e&(e-1))):
				k=__bsf(e)+1
				if (k>mx_sz):
					mx_sz=k
			else:
				k=__popcnt(e)-2
				if (k<=vil):
					vil=k+1
					vi=realloc(vi,vil)
					vi[k]=1
				else:
					vi[k]+=1
			mx|=e
	if (mx&(mx+1)):
		raise RuntimeError("Not All Identifiers Used")
	vil+=1
	vi=realloc(vi,vil)
	off=0
	for i in range(0,vil-1):
		j=vi[i]
		vi[i]=off
		off+=j
	vi[vil-1]=off
	o=0
	om=mx
	a=alloc(w)
	na=alloc(w)
	v=alloc(off)
	for i in range(0,off):
		v[i]=0
	for i in range(0,w):
		a[i]=0
		for j in range(0,h):
			e=A[i][j]
			if (not (e&(e-1))):
				a[i]|=e
			else:
				k=__popcnt(e)-2
				for l in range(vi[k],vi[k+1]):
					if (v[l]==0):
						a[i]|=1<<(l+mx_sz)
						v[l]=e
						break
					if (v[l]==e):
						a[i]|=1<<(l+mx_sz)
						break
		na[i]=a[i]
	while (True):
		i=0
		m=1
		for j in range(0,off+mx_sz):
			k=i
			t=na[i]
			sk=False
			while (not (t&m)):
				k+=1
				if (k==w):
					sk=True
					break
				t=na[k]
			if (not sk):
				na[k]=na[i]
				na[i]=t
				for k in range(i+1,w):
					if (na[k]&m):
						na[k]^=na[i]^m
				i+=1
				if (i==w):
					break
			m<<=1
		s=0
		m=b
		while (m):
			s^=na[__bsf(m)]
			m&=m-1
		if (vil==0):
			return o|(s&om)
		f=0
		for i in range(vi[vil-2],vi[vil-1]):
			k=v[i]
			if (k==0):
				continue
			m=1<<(i+mx_sz)
			if (s&m):
				f|=2
				v[i]=0
				o|=k
				om&=~k
				m|=k
				im=~m
				for j in range(0,w):
					b^=__parity(a[j]&m)<<j
					a[j]&=im
			else:
				f|=1
		if (not (f&1)):
			vil-=1
		elif (not (f&2)):
			raise RuntimeError("Guess 'and' Variables")
		for i in range(0,w):
			na[i]=a[i]



o=solve([[0b001,0b010,0b011],[0b001,0b010,0b100]],0b01)
print(f"a^b^(a&b)=1, a^b^c=0 -> a={o&1}, b={(o>>1)&1}, c={o>>2}")

