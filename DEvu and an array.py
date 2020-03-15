n,q=[int(x) for x in input().split()]
a=sorted([int(x) for x in input().split()])
for _ in range(q):
    qu=int(input())
    if qu in range(a[0],a[-1]+1):
        print("Yes")
    else:
        print("No")