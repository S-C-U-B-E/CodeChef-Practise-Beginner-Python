for _ in range(int(input())):
    sal=float(input())
    hra,da=0.0,0.0
    if sal<1500:
        hra=0.1*sal
        da=0.9*sal
    elif sal>=1500:
        hra=500
        da=0.98*sal
    print(sal+hra+da)
