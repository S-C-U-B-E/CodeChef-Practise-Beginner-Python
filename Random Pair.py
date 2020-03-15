for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    lsa=list(set(a))
    lsa.sort()
    maxc,max2c=a.count(lsa[-1]),0
    if len(lsa)!=1:
        max2c=a.count(lsa[-2])
    if maxc==1:
        print("{:.8f}".format(max2c/((n*(n-1))/2)))
    else:
        print("{:.8f}".format(((maxc * (maxc - 1)) / 2) / ((n * (n - 1)) / 2)))