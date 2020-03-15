for _ in range(int(input())):
    n=int(input())
    s=list(input())
    LOL=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    i=0
    while i+1<n:
        temp=s[i]
        s[i]=s[i+1]
        s[i+1]=temp
        i+=2
    #print(s)
    for j in range(n):
        s[j]=LOL[-(LOL.index(s[j])+1)]
    print(str.join('',s))