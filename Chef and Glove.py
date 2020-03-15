for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    g=list(map(int,input().split()))
    front,back=True,True
    for i in range(n):
        if l[i]>g[i]:
            front=False
            break
    g.reverse()
    for i in range(n):
        if l[i]>g[i]:
            back=False
            break
    if front and back:
        print("both")
    elif front:
        print("front")
    elif back:
        print("back")
    else:
        print("none")