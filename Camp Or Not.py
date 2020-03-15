for _ in range(int(input())):
    da=int(input())
    d=[0]*40
    for i in range(da):
        x,z=map(int,input().split())
        d[x]=z

    q=int(input())
    for i in range(q):
        x, z = map(int, input().split())
        if sum(d[0:x+1])>=z:
            print("Go Camp")
        else:
            print("Go Sleep")