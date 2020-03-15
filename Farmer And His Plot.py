import math as ma
for _ in range(int(input())):
    n,m=map(int,input().split())
    print(int((m*n)//ma.pow(ma.gcd(n,m),2)))
