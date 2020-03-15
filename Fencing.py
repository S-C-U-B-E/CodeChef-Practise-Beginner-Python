for _ in range(int(input())):
    n,m,ck=map(int,input().split())
    a=[[]]
    pl=[]
    r1,rprev=-2,0
    fu=ck*4
    for _ in range(ck):
        pl.append(list(map(int,input().split())))
    pl.sort()
    for i in pl:
        r,c=i[0],i[1]
        if r!=r1:
            a.append([])
            rprev=r1
            r1=r
        a[-1].append(c)
        if c-1 in a[-1]:
            fu-=2
        if (c in a[-2]) and r-rprev==1:
            fu-=2
    print(fu)

#"Those who break the rules are scum, that's true, but those who abandon their friends are worse than scum."