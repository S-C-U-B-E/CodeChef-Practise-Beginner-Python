for _ in range(int(input())):
    n,x=map(int,input().split())
    a=[int(x) for x in input().split()]
    if any(i>=x for i in a ):
        print("YES")
    else:
        print("NO")