for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    flag=0
    if a==c and b==d:
        print("Yes")
        continue
    elif a>c and b>d:
        print("No")
        continue
    else:
        while True:
            if d-c>0:
                d-=c
            else:
                c-=d
            if c==a and d==b:
                flag=1
                break
            if c<a or d<b:
                break
    if flag:
        print("Yes")
    else:
        print("No")