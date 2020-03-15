t=int(input())
a=[]
for _ in range(t):
    a.append(int(input()))
a.sort()
print(*a,sep="\n")