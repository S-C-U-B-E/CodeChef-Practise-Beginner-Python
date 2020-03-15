for _ in range(int(input())):
    mydik={"mon":1,"tues":2 ,"wed":3, "thurs":4, "fri":5, "sat":6, "sun":7}
    inp=input()
    w=int(inp.split()[0])
    s=inp.split()[1]
    r=w-28
    i=1
    d=[]
    while i<=7:
        if i<mydik[s]or r==0:
            d.append(4)
        else:
            d.append(5)
            r-=1
        i+=1
    if r!=0:
        for i in range(r):
            d[i]=5
    print(*d)
