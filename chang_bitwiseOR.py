for _ in range(int(input())):
    cost=0
    n=int(input())
    A=[int(x) for x in input().split()]
    for i in range(n):
        cost |=A[i]
    print(cost)