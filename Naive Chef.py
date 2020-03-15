for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=[int(x) for x in input().split()]
    ca,cb=x.count(a),x.count(b)
    print("{:.10f}".format((ca*cb)/n**2))
    