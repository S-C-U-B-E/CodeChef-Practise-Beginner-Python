for _ in range(int(input())):
    n=int(input())
    d=[int(x) for x in input().split()]
    print(n-(len(d)-len(set(d))))