for _ in range(int(input())):
    s=input()
    c=list(set(s))
    l=[]
    for i in c:
        l.append(s.count(i))
    noty=0
    l.sort()
    #print(l)
    if len(l)<3:
        print("Dynamic")
    else:
        for i in range(2,len(l)):
            if i==3:
                if not l[3]==l[2]+l[1] and not l[3]==l[2]+l[0]:
                    noty=1
                    break
            elif l[i-1]+l[i-2]!=l[i]:
                noty=1
                break
        if noty:
            print("Not")
        else:
            print("Dynamic")
