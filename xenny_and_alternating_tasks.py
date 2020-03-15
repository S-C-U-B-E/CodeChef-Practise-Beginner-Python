for _ in range(int(input())):
    n=int(input())
    min1=min2=0
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    for i in range(n):
        if i%2==0:
            min1+=X[i]
            min2+=Y[i]
        else:
            min1+=Y[i]
            min2+=X[i]
    if min1<=min2:
        print(str(min1))
    else:
        print(str(min2))
