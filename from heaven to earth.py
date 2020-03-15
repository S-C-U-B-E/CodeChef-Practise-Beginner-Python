from math import sqrt
for _ in range(int(input())):
    n,v1,v2=map(int,input().split())
    ans=["Stairs","Elevator"]
    print(ans[0]*bool(((sqrt(2)*n)/v1)<2*(n/v2))+ans[1]*bool(((sqrt(2)*n)/v1)>=2*(n/v2)))