for z in range(int(input())):
    l,k=map(int,input().split())
    s=0
    if k>l:
        print("Case "+str(z+1)+": 0")
    elif k==l:
        print("Case "+str(z+1)+": 1")
    else:
        if l<=4:
            n=1
        else:
            n=(l-4)+1
        for i in range(n+1,0,-1):
            if i-k>0:
                s+=i-k
            else:
                break
        #print(s)

        print("Case "+str(z+1)+": "+str(s+3))


"""for z in range(int(input())):
    l,k=map(int,input().split())
    s=0
    for i in range(l+1,0,-1):
        if i-k>0:
            s+=i-k
        else:
            break
    print("Case "+str(z+1)+": "+str(s))
"""

