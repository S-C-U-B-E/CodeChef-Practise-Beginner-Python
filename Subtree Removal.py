for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    l,su=[],0
    forbidden=[0]*n
    for _ in range(n-1):
        t=list(map(int,input().split()))
        l.append(t)
    l.sort()
    c=0
    pos=[0]*(n+1)
    pos[0]=1
    for i in l[-1::-1]:
            a[i[0]-1]+=a[i[1]-1]
    ans=a[0]

    for i in l:
        if i[0]==1 or pos[i[0]-1]==1:
            pos[i[1]-1]=i[0]
        else:
            pos[i[1]-1]=pos[i[0]-1]
    #print(pos)

    ns=[]
    for _ in range(l[(pos.count(1)-1)-1][1]):
        ns.append([])
    for i in range(1,n):
        ns[pos[i]-1].append(a[i])
    #print(ns)

    p1=0
    if ans-ans-k>=ans:
        p1=ans-ans-k

    for i in range(1,len(ns)):
        m=min(ns[i])
        #print(m)
        m=min(m,ns[0][i-1])
        #print(m,ns[0][i-1])
        if m<0 and abs(m)-k>0:
            ans=ans+(abs(m)-k)
    print(max(p1,ans))

    """for i in l:
        if forbidden[i[0]-1]!=1:
            if a[i[1]-1]<0 and abs(a[i[1]-1])-k>0:
                forbidden[i[1]-1]=1
                ans+=abs(a[i[1]-1])
                c+=1
        else:
            forbidden[i[1]-1]=1


    print(ans-(k*c))"""