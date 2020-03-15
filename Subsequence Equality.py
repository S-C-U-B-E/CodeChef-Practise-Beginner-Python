for _ in range(int(input())):
    s=input()
    flag=0
    for i in range(len(s)-2):
        if s.count(s[i])>=2:
            print("yes")
            flag=1
            break
    if not flag:
        print("no")