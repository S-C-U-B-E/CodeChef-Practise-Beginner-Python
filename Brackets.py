for _ in range(int(input())):
    a=input()
    balance = 0
    max_balance = 0
    for i in range(len(a)):
        if a[i] == '(' :balance+=1
        if a[i] == ')' :balance-=1
        max_balance = max(max_balance, balance)
    for i in range(max_balance):
        print("(",end='')
    for i in range(max_balance):
        print(")",end='')
    print()