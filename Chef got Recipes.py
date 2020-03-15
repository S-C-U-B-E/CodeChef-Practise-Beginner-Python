for _ in range(int(input())):
    n=int(input())
    c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #subc=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cou=0
    vow={'a','e','i','o','u'}
    l=[{'a'}, {'a', 'e'}, {'i', 'a', 'e'}, {'i', 'a', 'e', 'o'}, {'i', 'a', 'e', 'u'}, {'a', 'e', 'o'},
     {'a', 'e', 'o', 'u'}, {'a', 'e', 'u'}, {'i', 'a'}, {'i', 'a', 'o'}, {'i', 'a', 'o', 'u'}, {'i', 'a', 'u'},
     {'a', 'o'}, {'a', 'o', 'u'}, {'a', 'u'}, {'e'}, {'i', 'e'}, {'i', 'e', 'o'}, {'i', 'e', 'o', 'u'}, {'i', 'e', 'u'},
     {'e', 'o'}, {'e', 'o', 'u'}, {'e', 'u'}, {'i'}, {'i', 'o'}, {'i', 'o', 'u'}, {'i', 'u'}, {'o'}, {'o', 'u'}, {'u'},
     {'i', 'o', 'e', 'u', 'a'},{}]
    for i in range(n):
        s=set(input())
        #print(s,vow-s)
        c[l.index(s)]+=1
    #print(c)

    """for i in range(len(l)-1):
        for j in range(len(l)):
            if l[j]!=l[i] and l[i].issubset(l[j]):
                subc[l.index(l[i])]+=c[l.index(l[j])]"""

    for i in range(len(l)):
        if c[i]!=0:
            if l[i]==vow:
                cou+=((n*c[i])-((c[i]*(c[i]+1))//2))
            else:
                #print("for " + str(l[i]))
                cou+=(c[l.index(vow-l[i])]*c[i])
                #print("core:"+str(c[l.index(vow-l[i])]*c[i]))
                for j in range(len(l)-2):
                    if (vow-l[i]).issubset(l[j]) and (vow-l[i])!=l[j]:
                        cou+=(c[l.index(l[j])]*c[i])
                        #print("subset wala:" + str(c[l.index(l[j])]*c[i]))
                #print(str(cou))
                c[i]=0
                #print(c)

    print(cou)