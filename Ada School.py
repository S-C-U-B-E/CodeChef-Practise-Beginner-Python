for _ in range(int(input())):
    n,m=map(int,input().split())
    if n==1 or m==1 or (m*n)%2!=0:
        print("NO")
    else:
        print("YES")