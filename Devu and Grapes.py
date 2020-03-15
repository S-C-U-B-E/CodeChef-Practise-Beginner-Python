for x in range(int(input())):
    n,m=map(int,input().split())
    b=[int(x) for x in input().split()]
    usm=0
    """for i in b:
        d=i//m
        usm+=min(abs(i-(d*m)),abs(i-((d+1)*m)))
    print(usm)
    usm=0"""
    for i in b:
        if i % m!= 0:
            d = i // m
            usm += min(abs(i - (d * m)), abs(i - ((d + 1) * m)))
    print(usm)
    """usm=0
    for i in b:
        if i % m != 0:
            d = i % m
            if i > m:
                usm += min(d, m - d)
            else:
                usm += m - d
    print(usm)"""