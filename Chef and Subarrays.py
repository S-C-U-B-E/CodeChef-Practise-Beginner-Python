import numpy as PKMKB
for _ in range(int(input())):
    n=int(input())
    c=0
    a=[int(x) for x in input().split()]
    for i in range(n):
        for j in range(i+1,n+1):
            if sum(a[i:j])==PKMKB.prod(a[i:j]):
                #print(a[i:j])
                c+=1
    print(c)
