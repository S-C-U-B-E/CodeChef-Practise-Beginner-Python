for _ in range(int(input())):
    n=int(input())
    a=[]
    maxy=[]

    for i in range(n):
       a.append(list(map(int,input().split())))

    for i in range(n):
        sumy=0
        i1=i
        for j in range(n-i):
            sumy+=a[j][i1]
            i1+=1
        maxy.append(sumy)
    #print(maxy)
    for i in range(1,n):
        sumy=0
        i1=i
        for j in range(n-i):
            sumy+=a[i1][j]
            i1+=1
        maxy.append(sumy)
    #print(maxy)
    print(max(maxy))