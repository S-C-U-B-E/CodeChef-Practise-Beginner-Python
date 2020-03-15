for _ in range(int(input())):
    n=int(input())
    s=input().upper()
    i=s.count('I')
    no=s.count('N')
    y=s.count('Y')
    if no==len(s) or (i!=0 and y!=0):
        print("NOT SURE")
    elif i==0 and y>0:
        print("NOT INDIAN")
    elif y==0 and i>0:
        print("INDIAN")