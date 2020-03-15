for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    while len(a)>2:
        for i in a:
            #print(a," i:"+str(i))
            temp=a.copy()
            temp.remove(i)
            for j in temp:

                if (i+j)%2==0:
                    #print(i,j,i+j)
                    a.append(i+j)
                    a.remove(i)
                    a.remove(j)
                    break
    #print("a:"+str(a))
    if len(a)==2 and (a[0]+a[1])%2!=0:
        print(2)
    else:
        print(1)