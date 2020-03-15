import sys
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    minu = sys.maxsize
    minx=0
    for i in range(n):
        sumu=sum(a[0:i+1])+sum(a[-(n-i):])
        if sumu<minu:
            minu=sumu
            minx=i+1
    print(minx)