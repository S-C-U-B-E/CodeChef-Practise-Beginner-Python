for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    s=list(set(a))
    s.sort()
    s.reverse()
    cont=0
    ar=1
    for i in s:
        if a.count(i)>1 and cont<2:
            ar*=i
            cont+=1
        if a.count(i)>3 and cont<2:
            ar*=i
            cont+=1
        if cont==2:
            print(ar)
            break
    if cont<2:print(-1)
