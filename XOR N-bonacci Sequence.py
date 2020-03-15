n,q=map(int,input().split())
f=[int(x) for x in input().split()]
xortab=[]
xor,xor1=0,0
for i in f:
    xor^=i
    xortab.append(xor)
xortab.append(0)
#print(xor)
for i in range(q):
    k=int(input())
    rem=k%(n+1)
    print(xortab[rem-1])