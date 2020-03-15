import sys
n=int(input())
c=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
min1,min2,min3=sys.maxsize,sys.maxsize,sys.maxsize
for i in range(n):
    if t[i]==1:
        if c[i]<min1:
            min1=c[i]
    elif t[i]==2:
        if c[i]<min2:
            min2=c[i]
    elif t[i]==3:
        if c[i]<min3:
            min3=c[i]
if min1+min2<min3:
    print(min1+min2)
else:
    print(min3)