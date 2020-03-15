for _ in range(int(input())):
    n=int(input())
    s=list(input())
    c=0
    nz,no=0,0

    for i in range(n):
        if s[i]=='0':
            nz+=1
        else:
            no+=1
        if nz>no:
            no+=1
            nz-=1
            c+=1
    print(c)
