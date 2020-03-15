for _ in range(int(input())):
    n,k=map(int,input().split())
    s=(k*(k+1))/2
    s+=(n-k)*1
    print(int(s))

