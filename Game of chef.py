for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    su,m=0,0
    for i in range(n):
        for j in range(i,n+1):
            su=sum(a[i:j])
            if su>m:
                m=su
    print(m)
