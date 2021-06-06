def _solve_xor(a,b):
	m=len(a)
	n=len(a[0])
	i=0
	for j in range(0,n):
		mx=i
		mx_v=a[i][j]
		while (mx_v==0):
			mx+=1
			if (mx==m):
				break
			mx_v=a[mx][j]
		if (mx_v!=0):
			for k in range(0,n):
				t=a[mx][k]
				a[mx][k]=a[i][k]
				a[i][k]=t
			for k in range(i+1,m):
				for l in range(j+1,n):
					a[k][l]^=a[i][l]&a[k][j]
				a[k][j]=0
			i+=1
			if (i==m):
				break
	o=[0 for _ in range(0,n)]
	for i in range(0,m):
		for j in range(0,n):
			o[j]^=b[i]&a[i][j]
	return o



def solve(b,*l):
	o=[]
	v=[]
	vm=[]
	vml=0
	a=[]
	for k in l:
		e=[0 for _ in range(0,len(v))]
		for se in k.split("^"):
			if (se not in v):
				while (len(vm)<len(se)):
					vm.append([])
					vml+=1
				vm[len(se)-1].append((se,len(v)))
				o.append(None)
				v.append(se)
				e.append(1)
			else:
				e[v.index(se)]=1
		a.append(e)
	for k in a:
		for _ in range(0,len(v)-len(k)):
			k.append(0)
	while (True):
		s=_solve_xor([e[:] for e in a],b[:])
		if (vml==1):
			for i in range(0,len(v)):
				if (o[i] is None):
					o[i]=s[i]
			om={}
			for i,k in enumerate(v):
				if (len(k)==1):
					om[k]=o[i]
			return om
		for k in vm[vml-1]:
			if (s[k[1]]==1):
				i=v.index(k[0])
				o[i]=1
				for j in range(0,len(a)):
					if (a[j][i]==1):
						a[j][i]=0
						b[j]^=1
				for e in k[0]:
					i=v.index(e)
					o[i]=1
					for j in range(0,len(a)):
						if (a[j][i]==1):
							a[j][i]=0
							b[j]^=1
			else:
				print("Unknown Combination!")
		vml-=1
		while (len(vm[vml-1])==0):
			vml-=1



print(solve([0,1],"a^b^c","a^b^ab"))
