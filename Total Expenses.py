for _ in range(int(input())):
    q,p=map(float,input().split())
    if q>1000:
        p=0.9*p
    print("%.6f"%(q*p))