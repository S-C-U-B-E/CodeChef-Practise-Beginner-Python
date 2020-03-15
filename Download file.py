for _ in range(int(input())):
    n,k=map(int,input().split())
    su=0
    for i in range(n):
        t,d=map(int,input().split())
        if k>t:
            k-=t
        else:
            t-=k
            k-=k
        if not k:
            su+=t*d
    print(su)