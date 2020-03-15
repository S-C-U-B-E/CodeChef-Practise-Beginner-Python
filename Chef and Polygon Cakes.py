import math
for _ in range(int(input())):
    n,a,k=map(int,input().split())
    num=(360*(n-2))-((2*a)*n)
    d=(n*(n-1))
    num=a*d+(k-1)*num
    print(int(num/math.gcd(num,d)),int(d/math.gcd(num,d)))
