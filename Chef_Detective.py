n=int(input())
r=[int(x) for x in input().split()]
r=set(r)
for i in range(n):
    if (i+1) not in r:
        print(i+1,end=" ")