"""for _ in range(int(input())):
    st=input()
    s=set(st)
    #print(s)
    c=[]
    sum=0
    for i in s:
        c.append(st.count(i))
    c.sort()
    for i in range(len(c)-1):
        sum+=c[i]
    if sum==c[len(c)-1]:
        print("YES")
    else:
        print("NO")"""
try:
    import collections
    m=int(input())
    while m:
         x=input()
         l=list(x)
         v=len(l)
         c=collections.Counter(l)
         k=list(c.values())
         u=max(k)
         print(u,v)
         if u == (v-u):
            print("YES")
         else:
            print("NO")
         m-=1
except:
    pass
