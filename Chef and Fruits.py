for _ in range(int(input())):
    a,o,k=map(int,input().split())
    if abs(a-o)<=k:
        print(0)
    else:
        print(abs(a-o)-k)