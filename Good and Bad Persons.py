for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    u,l=0,0
    for x in s:
        if x.isupper():
            u+=1
        else:
            l+=1
    if u<=k and l>k:
        print("chef")
    elif l<=k and u>k:
        print("brother")
    elif u<=k and l<=k:
        print("both")
    else:
        print("none")
