s=input()
n=int(input())

for _ in range(n):
    flag = 0
    w=set(input())
    for i in w:
        if i not in s:
            print("No")
            flag=1
            break
    if not flag:print("Yes")