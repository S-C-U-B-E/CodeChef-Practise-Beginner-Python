for _ in range(int(input())):
    n=int(input())
    s1=list(input().upper())
    s2=list(input().upper())
    w=[int(x) for x in input().split()]
    c=0
    uc=0
    for i in range(n):
        if s1[i]==s2[i]:
            c+=1
    if c==0 or len(set(w))==1:
        print(w[0])
        continue
    elif c==n:
        print(w[n])
        continue
    else:
        print(max(w[:c+1]))