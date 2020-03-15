for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    maxi=0
    for i in range(n-k+1):
        if sum(a[i:i+k])>maxi:
            maxi=sum(a[i:i+k])
    print(maxi)