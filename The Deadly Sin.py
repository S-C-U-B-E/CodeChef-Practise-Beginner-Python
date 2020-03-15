import math as ma
for _ in range(int(input())):
    x,y=map(int,input().split())
    print(2*ma.gcd(x,y))