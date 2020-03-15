for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    count=0
    if b<a or d<c:
        print(0)
    else:
        for i in range(a,b+1):
            if i<d:
                count+=d-max(c,i+1)+1
            else:
                break
        print(count)
#aftr stdyn editorial :(