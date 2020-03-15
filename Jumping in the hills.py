for _ in range(int(input())):
    n,u,d=map(int,input().split())
    h=[int(x) for x in input().split()]
    para,i=0,0
    while i<n-1:
        if h[i+1]<=h[i]:
            if h[i]-h[i+1]<=d:
                i+=1
            elif para==0:
                para=1
                i+=1
            else:
                break
        elif h[i+1]>=h[i]:
            if h[i+1]-h[i]<=u:
                i+=1
            else:
                break

    print(i+1)