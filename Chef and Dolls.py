for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
       a.append(int(input()))
    s=set(a)
    for i in s:
        if a.count(i)%2!=0:
            print(i)
            break
