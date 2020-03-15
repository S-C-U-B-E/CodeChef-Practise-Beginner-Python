import math
for _ in range(int(input())):
    n,x,y,k=[int(x) for x in input().split()]
    cx=int(n/x)
    cy=int(n/y)
    clcm=int(n/((x*y)//math.gcd(x,y)))
    #print(cx,cy,clcm)
    if cx+cy-(2*clcm)>=k:
        print("Win")
    else:
        print("Lose")
