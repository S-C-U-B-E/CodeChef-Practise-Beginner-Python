for _ in range(int(input())):
    x1,x2,x3,v1,v2=map(int,input().split())
    dx1=abs(x3-x1)
    dx2 = abs(x3 - x2)
    t1,t2=dx1/v1,dx2/v2
    if t1<t2:
        print("Chef")
    elif t2<t1:
        print("Kefa")
    else:
        print("Draw")