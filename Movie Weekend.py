for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    r = [int(x) for x in input().split()]
    maxmul=-1
    maxr=-1
    for i in range(n):
        if l[i]*r[i]>maxmul:
            maxmul=l[i]*r[i]
    for i in range(n):
        if l[i]*r[i]==maxmul:
            if r[i]>maxr:
                maxr=r[i]

    print(r.index(maxr)+1)
