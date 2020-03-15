def series(n1,k1):
    s=0
    if n1<=k1:
        return 1
    else:
        for i in range(1,k1+1):
            s+=series(n1-i,k1)
    return s

n,k=map(int,input().split())
ans=series(n,k)
print(ans%1000000007)