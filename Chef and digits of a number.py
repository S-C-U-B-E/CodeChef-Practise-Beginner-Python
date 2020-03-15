for _ in range(int(input())):
    n=input()
    if n.count('1')==1 or n.count('0')==1:
        print("Yes")
    else:
        print("No")