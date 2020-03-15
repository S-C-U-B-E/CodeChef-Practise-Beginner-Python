for _ in range(int(input())):
    r=int(input())
    a=[]
    for _ in range(r):
        a.append([int(x) for x in input().split()])
    st=a[0]
    temp=[]
    for i in range(1,r):
        k=0
        for j in st:
            if k>0:
                if j+a[i][k]>temp[k]:
                    temp[k]=j+a[i][k]
            else:
                temp.append(j+a[i][k])
            temp.append(j+a[i][k+1])
            k+=1
        st=temp.copy()
        temp=[]
        #print(st)
    print(max(st))
