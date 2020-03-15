import numpy as np
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append([int(c) for c in input().split()])
    p=a.copy()
    #print(p)
    mi=9999
    x=1
    start,temp=a[0],[]
    #print("start="+str(start))
    #print("pos of start in p= " + str(p.index(start) + 1))
    #print(str(a[0])+" removed")
    a.remove(a[0])
    for _ in range(n-1):
        l = len(a)
        #print(*a)
        #print("len(a)= "+str(l))
        for i in range(l):
           if min(abs(start[0]-a[i][0]),abs(start[1]-a[i][1]))<mi:
               mi=min(abs(start[0]-a[i][0]),abs(start[1]-a[i][1]))
               temp=a[i]
               #print(str(temp) + " at " + str(a.index(temp) + 1))
               #print(mi)

        start=temp
        #print("start="+str(start))
        #print("p= "+str(p))
        #print("pos of start in p= "+str(p.index(start)+1))
        x = np.bitwise_xor(x, p.index(start)+1)
        #print("x= "+str(x))
        #print(str(a[a.index(start)]) + " removed")
        a.remove(a[a.index(start)])
        mi=9999
    print(x)