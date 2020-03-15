for _ in range(int(input())):
    n,x,s=map(int,input().split())
    kidnap=x
    for i in range(s):
        a,b=map(int,input().split())
        if kidnap==a:
            kidnap=b
        elif kidnap==b:
            kidnap=a
    print(kidnap)