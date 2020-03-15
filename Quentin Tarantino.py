for _ in range(int(input())):
    n=int(input())
    ch=[int(x) for x in input().split()]
    nch=ch.copy()
    ch.sort()
    if len(set(ch))<len(ch) or (max(ch)*(max(ch)+1))/2!=sum(ch) or ch==nch:
        print("no")
        continue
    print("yes")