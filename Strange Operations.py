for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    s=(2*sum(a))+1
    if (((k-1)*s)+2)%2==0:print("even")
    else:print("odd")