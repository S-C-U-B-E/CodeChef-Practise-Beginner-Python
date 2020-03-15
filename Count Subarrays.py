for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.append(-1)
    s=0
    i,j,c=0,1,0
    while j<len(a):
        if a[j]<a[j-1]:
            s+=((j-i)*(1+j-i))/2
            i=j
        j+=1
    print(int(s))