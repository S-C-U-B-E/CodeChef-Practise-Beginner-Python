for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if n%2==0:
        if abs(a)==abs(b):
            print(0)
        elif abs(a)>abs(b):
            print(1)
        else:
            print(2)
    else:
        if a==b:
            print(0)
        elif a>b:
            print(1)
        else:
            print(2)