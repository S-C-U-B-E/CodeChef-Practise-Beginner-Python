for _ in range(int(input())):
    n,x=map(int,input().split())
    s=input()
    a=[x]
    for i in s:
        if i=='R':
            x+=1
        elif i=='L':
            x-=1
        if x not in a:
            a.append(x)
    #print(a)
    print(len(a))