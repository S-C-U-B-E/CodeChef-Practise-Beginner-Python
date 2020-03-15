import math as ma
for _ in range(int(input())):
    n,k,s=map(int,input().split())
    d=s-(s//7)
    req=k*s
    got=n*d
    daysononebox=n/k
    if got>=req:
        print(int(ma.ceil(s/daysononebox)))
    else:
        print(-1)