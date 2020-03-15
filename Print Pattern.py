import numpy as np
for _ in range(int(input())):
    n=int(input())
    x=np.zeros((n,n))
    i,j,c=0,0,0
    while i<=n-1 and j<=n-1:
        tempi = i
        tempj = j
        while tempi<=j:
            c+=1
            x[tempi][tempj]=int(c)
            tempj-=1
            tempi+=1
        if j!=n-1:
            i=0
            j+=1
        else:
            i+=1
            j=n-1

    for i in range(n):
        print(*list(map(int,x[i])))