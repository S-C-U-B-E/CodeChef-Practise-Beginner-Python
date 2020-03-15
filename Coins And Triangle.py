for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(1,n+1):
        if (i*(i+1))//2<=n:
            c=i
        else:
            break
    print(c)