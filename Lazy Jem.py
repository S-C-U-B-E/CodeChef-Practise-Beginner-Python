for _ in range(int(input())):
    n,b,m=map(int,input().split())
    su=0
    while n!=0:
        p=int((n/2)*(n%2==0)+((n+1)/2)*(n%2!=0))
        su+=p*m+b*(n//2!=0)
        m*=2
        n-=p
    print(su)