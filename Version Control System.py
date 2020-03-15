for _ in range(int(input())):
    n,m,k=map(int,input().split())
    ig=set([int(x) for x in input().split()])
    tc=set([int(x) for x in input().split()])
    print(len(ig.intersection(tc)),n-len(ig.union(tc)))