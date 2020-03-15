for _ in range(int(input())):
    n,k=map(int,input().split())
    maxc=0
    for i in range(1,k+1):
        if n%i>maxc:
            maxc=n%i
    print(maxc)
