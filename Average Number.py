for _ in range(int(input())):
    n,k,v=map(int,input().split())
    a=[int(x) for x in input().split()]
    tot=(n+k)*v-sum(a)
    ele=tot/k
    ele2=tot//k
    if ele==ele2 and ele>=1:
        print(ele2)
    else:
        print(-1)