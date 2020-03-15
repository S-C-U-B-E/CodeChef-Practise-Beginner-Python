for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    sumy=0
    joined=0
    for i in range(n):
        if sumy>=a[i]:
            sumy+=1
            joined+=1
    print(joined)