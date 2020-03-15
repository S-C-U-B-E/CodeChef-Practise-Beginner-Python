for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    d,c=[],[]
    for i in range(n):
        if a[i]>b[i]:
            d.append(a[i]-b[i])
            c.append(i)
        else:
            d.append(b[i]-a[i])
            c.append(i)
    print(d)
    print(c)

    for i in range(n-1):
        for j in range(i+1,n):
            if d[i]<d[j]:
                temp=d[j]
                d[j]=d[i]
                d[i]=temp
                temp=c[j]
                c[j]=c[i]
                c[i]=temp
    print(d)
    print(c)


