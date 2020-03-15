for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x)for x in input().split()]
    a.sort()
    if k==0:print(sum(a)/n)
    else: print( sum(a[k:-k])/(n-(2*k)) )
   