for _ in range(int(input())):
    tot=0
    n=[int(x) for x in input().split()]
    st=sorted(set(input().lower()))
    for i in range(len(st)):
        st[i]=ord(st[i])
    for i in range(97,123):
        if i not in st:
            tot+=n[i-97]
    print(tot)