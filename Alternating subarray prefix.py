for _ in range(int(input())):
    n=int(input())
    a=[0 if int(x)<0 else 1 for x in input().split()]
    i,j,k=0,0,0
    while i <=(n-1):
        s=0
        j=i
        while j<=(n-1):
            if j<n-1:k=j+1
            if j==n-1:k=j
            if a[j]!=a[k]:
                s+=1
                j+=1
                continue
            if a[j]==a[k]:
                break
        s+=1
        for q in range(s,0,-1):
            print(q,end=' ')
        i=k
        if j==n-1:
            break
    print()