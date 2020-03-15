for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    c=0
    for i in a:
        if i>1:
            c+=1
    if c<=k:
        print("YES")
    else:
        print("NO")