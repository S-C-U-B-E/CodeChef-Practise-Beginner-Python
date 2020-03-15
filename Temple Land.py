for _ in range(int(input())):
    n=int(input())
    h=[int(x) for x in input().split()]
    if n%2==0:
        print("no")
        continue
    else:
        m=n//2
        if h[0]==1 and h[n-1]==1:
            for i in range(m):
                if h[i]-h[i+1]!=-1 or h[-(i+1)]-h[-(i+1)-1]!=-1:
                    print("no")
                    break
                elif i==m-1:
                    print("yes")
        else:
            print("no")