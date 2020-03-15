for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    if x1==x2:
        print("up"*bool(y2>y1)+"down"*bool(y2<y1))
    elif y1==y2:
        print("right"*bool(x2>x1)+"left"*bool(x2<x1))
    else:
        print("sad")
