for _ in range(int(input())):
    n=int(input())
    s,x=input().split()
    c=0
    ind=[-1]
    for i in range(n):
        if s[i]==x:
            ind.append(i)
    for i in range(1,len(ind)):
        st=ind[i]-ind[i-1]
        f=n-ind[i]
        c+=(st*f)
    print(c)


#"A Shinobi's life is not measured by how they lived but rather what they managed to accomplish before their death." - The Jiraiya <3
