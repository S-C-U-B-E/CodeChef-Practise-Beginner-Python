for _ in range(int(input())):
    n1,p=input().split()
    n=int(n1)
    a=[int(x) for x in input().split()]
    if a[0]%2==0 and n==1 and p=='Dee':
        print("Dee")
    else:
        print("Dum")