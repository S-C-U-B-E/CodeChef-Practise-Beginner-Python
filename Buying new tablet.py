for _ in range(int(input())):
    n,b=map(int,input().split())
    maxy=-1
    for i in range(n):
        w,h,p=map(int,input().split())
        if p<=b:
            a=w*h
            if a>maxy:
                maxy=a
    if maxy==-1:
        print("no tablet")
    else:
        print(maxy)