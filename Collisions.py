# cook your dish here
for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    a=[]
    c=0
    for _ in range(n):
        a.append([int(i) for i in input()])
    for i in range(m):
        for j in range(n):
            if a[j][i]==1:
                for k in range(j+1,n):
                    if a[k][i]==1:
                        c+=1
    print(c)

