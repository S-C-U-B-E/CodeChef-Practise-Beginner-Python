def operation(st,pos,di):
    st=st.replace(st[pos],'',1)
    st+=di
    return st

for _ in range(int(input())):
    n,d=input().split()
    i=len(n)-1
    if n[-1]>d:
        n=operation(n,len(n)-1,d)
    while i>0:
        if n[i]<n[i-1]:
            n=operation(n,i-1,d)
        elif n[i]>d:
            n = operation(n,i,d)
        else:
            i-=1
    print(n)