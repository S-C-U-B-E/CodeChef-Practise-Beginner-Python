for _ in range(int(input())):
    n,k,e,m=map(int,input().split())
    a=[]
    for _ in range(n-1):
        temp=[int(x) for x in input().split()]
        a.append(sum(temp))
    a.sort()
    a.reverse()
    s=[int(x) for x in input().split()]
    ssu=sum(s)
    t=a[k-1]+1
    r=t-ssu
    if r<=0:
        print(0)
    elif r<m:
        print(r)
    else:
        print("Impossible")