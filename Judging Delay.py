for _ in range(int(input())):
    n=int(input())
    c=0
    for _ in range(n):
        s,j=map(int,input().split())
        if j-s>5:
            c+=1
    print(c)