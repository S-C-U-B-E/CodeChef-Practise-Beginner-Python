for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    print(len(set(a).intersection(set(b))))