for _ in range(int(input())):
    m,x,y=map(int,input().split())
    t=x*y
    a=[int(x) for x in input().split()]
    a.sort()
    strt,s=1,0
    for i in range(m):
        if a[i]>strt:
            r=a[i]-strt
            if r>=t:
             s+=r-t
        strt=a[i]+t+1
        if strt>100:
            break
    if strt<=100:
        s+=100-strt+1
    print(s)
