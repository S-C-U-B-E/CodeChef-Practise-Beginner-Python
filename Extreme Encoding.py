for j in range(int(input())):
    n=int(input())
    a,b=[],[]
    for i in range(n):
        u=int(input())
        a.append(u&0xfff)
        b.append(u>>16)
    print("Case "+str(j+1)+":")
    print(*a)
    print(*b)





"""x,n=map(int,input().split())
    n=n<<(1<<(1<<(1<<1)))
    x=x|n
    print(n)
    print(x)
    x1=x-n
    n=(((((n>>11)>>1)>>1)>>1)>>1)>>1   #just made trial error until it giving the same lol ;)
    print(x1,n)"""