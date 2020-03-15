for _ in range(int(input())):
    n=int(input())
    s=input().upper()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    print(n-max(r,g,b))