for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    s,maxy=0,[]
    for i in range(n):
        for j in range(i,n,k):
            s+=a[j]
        maxy.append(s)
        s=0
    print(max(maxy))