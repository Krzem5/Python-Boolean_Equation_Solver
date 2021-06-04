def solve_xor(a,b):
	l=len(a)
	h=0
	k=0
	while (h<l and k<l):
		mx=0
		mx_v=0
		for i in range(h,l):
			if (a[i][k]>mx_v):
				mx=i
				mx_v=a[i][k]
		if (mx_v!=0):
			a[h],a[mx]=a[mx],a[h]
			b[h],b[mx]=b[mx],b[h]
			for i in range(h+1,l):
				for j in range(k+1,l):
					a[i][j]^=(a[h][j]&a[i][k])
				b[i]^=a[i][k]&b[k]
				a[i][k]=0
			h+=1
		k+=1
	for i in range(l-1,-1,-1):
		for j in range(l-1,i,-1):
			b[i]^=b[j]&a[i][j]
	return b



print(solve_xor([[1,1,1],[1,1,0],[0,1,1]],[1,0,1]))
