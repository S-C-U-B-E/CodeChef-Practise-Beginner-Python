for _ in range(int(input())):
    a=[int(x) for x in input().split()]
    a.remove(len(a)-1)
    print(max(a))