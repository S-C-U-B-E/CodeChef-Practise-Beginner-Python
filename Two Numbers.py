for _ in range(int(input())):
    a,b,n=map(int,input().split())
    print((max(a,b)//min(a,b))*bool(n%2==0)+(max(2*a,b)//min(2*a,b))*bool(n%2!=0))