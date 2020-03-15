for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    r=[]
    c=[]
    for i in range(k):
        s=list(input().split())
        r.append(int(s[0]))
        c.append(int(s[1]))
    for i in range(n):
        if i+1 not in r:
            r.append(i+1)
            for j in range(n):
                if j+1 not in c:
                    c.append(j+1)
                    break
    print(len(r)-k,end=" ")
    for i in range(k,len(r)):
        print(r[i],end=" ")
        print(c[i],end=" ")
    print()