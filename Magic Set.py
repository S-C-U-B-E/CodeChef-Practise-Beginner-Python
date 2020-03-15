for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[int(x) for x in input().split()]
    c=0
    for i in a:
        if i%m==0:
            c+=1
    print(2**c-1)