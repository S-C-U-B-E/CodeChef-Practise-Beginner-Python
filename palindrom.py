s="SORES"

def pal(st):
    l=len(st)
    for i in range(int(l/2)):
        print(st[i])
        print(st[-(i+1)])
        if st[i]!=st[-(i+1)]:
            return 0
    return 1
"""for _ in range(int(input("ENTER N: "))):
    s=[]
    print("ENTER 9 STRINGS :  ")
    for _ in range(9):
        s.append(input())
    for v in range(9):
        print("SENT: "+str(s[v]),end="......")
        t=pal(s[v])
        if t:
            print("PALINDROM")
        else:
            print("NON_PALINDROM")"""

t=pal(s)
if t:
    print("PALINDROM")
else:
    print("NON_PALINDROM")