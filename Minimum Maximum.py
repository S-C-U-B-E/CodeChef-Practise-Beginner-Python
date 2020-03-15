for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    print(min(*a)*(n-1))
