for _ in range(int(input())):
    a,b,c,x,y=map(int,input().split())
    possible=0
    if x>=a and y>=b:
        if c==(x-a)+(y-b):
            possible=1
    elif x>=b and y>=a:
        if c==(x-b)+(y-a):
            possible=1
    elif x>=a and y>=c:
        if b==(x-a)+(y-c):
            possible=1
    elif x>=c and y>=a:
        if b==(x-c)+(y-a):
            possible=1
    elif x>=b and y>=c:
        if a==(x-b)+(y-c):
            possible=1
    elif x>=c and y>=b:
        if a==(x-c)+(y-b):
            possible=1

    if possible:
        print("YES")
    else:
        print("NO")
