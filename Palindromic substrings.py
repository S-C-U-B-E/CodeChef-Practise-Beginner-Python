for _ in range(int(input())):
    a=input()
    b=input()
    pal=False
    for i in a:
        if i in b:
            print("Yes")
            pal=True
            break
    if not pal:
        print("No")