for _ in range(int(input())):
    a,b=map(int,input().split())
    s1=0
    s=1
    while a>0 or b>0:
        q=a%10
        w=b%10
        s1=s1+(s*((q+w)%10))
        s=s*10
        a=a//10
        b=b//10
    print(s1)

