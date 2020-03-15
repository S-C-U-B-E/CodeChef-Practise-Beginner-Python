for j in range(int(input())):
    m,n=map(int,input().split())
    rx, ry = map(int, input().split())
    l=int(input())
    s=input()
    x,y=0,0
    for i in s:
        if i=='U':
            y+=1
        if i=='D':
            y-=1
        if i=='R':
            x+=1
        if i=='L':
            x-=1
    if (x<0 or y<0) or (x>m or y>n):
        print("Case "+str(j+1)+": DANGER")
    elif x==rx and y==ry:           #'or' karke rakha tha bhaaagwaaaan :(
                                    #bhagwaan: "kuch na ho payga re tera aagar isme bhi WA aya toh -_-"
                                    #bhagwaan: "aur kitna insult karwayega re khudka!!!!!"
                                    #me: "i never give up -_0"
        print("Case "+str(j+1)+": REACHED")
    else:
        print("Case "+str(j+1)+": SOMEWHERE")