"""a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]

for i in a:
    if i in b:
        print(i)"""

temp=[]
for i in range(9999):
    temp = str(i)
    s=0
    for t in temp:
        s+=int(t)**(len(temp))
        """print(s)"""
    if s==i:
        print(i)