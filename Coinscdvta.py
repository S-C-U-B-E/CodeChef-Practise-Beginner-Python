n=int(input())
dict={5:0,2:0,1:0}
x=1
r,t=0,0
while x<=n:
    r=5 * dict[5] + 2 * dict[2] + 1 * dict[1]
    if r>=x:
        x+=1
        continue
    else:
        d=[]
        for i in [1,2,5]:
            if i<=x:
                d.append(i)
        mr=0
        for i in d:
            if (i+r)>mr and i+r<=n:
                mr= i+r
                t=i
        dict[t]+=1
        x+=1
print(sum(dict.values()),dict[5],dict[2],dict[1])