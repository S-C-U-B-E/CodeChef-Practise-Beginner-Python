n,k=map(int,input().split())
a=[int(c) for c in input().split()]
p,mul,visited,ans=[],[],[],[]
mod=1000000007
for _ in range(n-1):
    p.append([])
    mul.append([])

for i in range(1,n):
    if a[i]-a[0]<=k:
        p[0].append(i)
        mul[0].append(a[0]*a[i])
    else:
        break
#print(p)
#print(mul)

for i in range(n-1):
    j=0
    #print("p[i] " + str(p[i]))
    while j<len(p[i]):
        #print("j "+str(j))
        #print("p[i][j] "+str(p[i][j]))
        if p[i][j] not in visited:
            for l in range(p[i][j]+1,n):
                if a[l]-a[p[i][j]] in range(1,k+1):
                    p[p[i][j]].append(l)
                    visited.append(p[i][j])
                    mul[p[i][j]].append((mul[i][j]*a[l])%mod)
                    if l==n-1:
                        ans.append(mul[p[i][j]][-1])
                else:
                    break
        j+=1
#print(p)
#print(mul)
#print(ans)
print(min(ans))