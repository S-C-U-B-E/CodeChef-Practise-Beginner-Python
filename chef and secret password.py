for _ in range(int(input())):
    n=int(input())
    s=input()
    """lmax=-1
    cmax=s.count(s[0])
    ctot=1
    ltot=len(s)
    pas=""
    for i in range(n//2+1):
        c=s.count(s[:i+1])
        l=len(s[:i+1])
        if cmax==c:
            if l>lmax:
                pas=s[:i+1]
                lmax=l
                cmax=c
    if ctot==cmax:
        if ltot>lmax:
            pas=s

    print(pas)"""
    st=s
    pas=""
    p=s[:len(s)//2]
    #print(p)
    cmax=0
    count=1
    lmax=-1
    while len(p)>=1:
        #print("s "+s)
        #print("p "+p)
        #print("s[len(s)//2+1:]  "+s[len(s)//2:])
        if p in s[len(s)//2:]:
            count=count*2
            l=len(p)
            if count>cmax:
                lmax=len(p)
                cmax=count
                pas=p
            elif count==cmax:
                if l>lmax:
                    lmax=l
                    pas=p
            #print("lmax "+str(lmax))
            #print("cmax "+str(cmax))
            s=p
            p = s[:len(s) // 2]
        else:
            p=p[:-1]
            #print(p)
    if cmax==0:
        print(st)
    else:
        print(pas)