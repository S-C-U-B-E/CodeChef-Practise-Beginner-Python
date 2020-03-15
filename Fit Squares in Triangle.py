for _ in range(int(input())):
    b=int(input())
    if b==1:
        print(0)
    else:
        c=(b//2)-1
        tot=(c*(c+1))/2
        print(int(tot))