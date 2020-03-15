for _ in range(int(input())):
    _=int(input())
    a=[int(x) for x in input().split()]
    s=0
    for i in a:
        if i==1:
            s+=1
        else:
            s-=1
        if s<0:
            break
    if s<0:
        print("Invalid")
    else:
        print("Valid")