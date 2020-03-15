for _ in range(int(input())):
    n=int(input())
    l=[]
    for _ in range(n):
        l.append(set(input()))
    print(len(set.intersection(*l)))