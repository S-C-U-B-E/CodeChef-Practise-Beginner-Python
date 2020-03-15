import math as ma
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    c=0
    subs=[a[i:i+j] for i in range(0,len(a)) for j in range(1,len(a)-i+1)]

    for i in subs:
        ori=i.copy()
        m=ma.ceil(k/len(i))
        for _ in range(m-1):
            i+=ori
        i.sort()
        x=i[k-1]
        f=ori.count(x)
        if f in ori:
            c+=1
    print(c)