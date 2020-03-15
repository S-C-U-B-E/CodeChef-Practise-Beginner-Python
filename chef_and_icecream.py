b=[0,1,3]

def count(a):
    if a<len(b):
        return b[a]
    else:
        p=(count(a-1)*2)+1-count(a-2)
        b.append(p)
        return p



for _ in range(int(input())):
    n=int(input())
    c=count(n)
    print(c)
    """i=len(b)-1
    if n<len(b):
        print(b[n])
    else:
        while i<=n:
           p=((b[i]*2)+1-b[i-1])%1000000007
           b.append(p)
           i=len(b)-1
        print(b[n])"""
