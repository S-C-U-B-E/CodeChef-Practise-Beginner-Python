for j in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    for i in range(n):
        if a[i] <= k:
            k-= a[i]
            a[i]= 1
        else:
            a[i]= 0
    for i in range(n):
        print(a[i], end="")
    print()


