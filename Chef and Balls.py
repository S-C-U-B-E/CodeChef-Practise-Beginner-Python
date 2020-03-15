for _ in range(int(input())):
    b,p=map(int,input().split())
    if b<p or p==0:
        print("cannot distribute")
    else:
        print(b//p)