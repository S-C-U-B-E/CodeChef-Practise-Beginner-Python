n=int(input())
w=int(input())
h=int(input())
th=int(input())
fh=int(input())
thsnd=int(input())

nthsnd=int(w/1000)
rem=w-1000*nthsnd

nfh=int(rem/500)
rem=rem-nfh*500

nth=int(rem/200)
rem=rem-nth*200

nh=int(rem/100)

if h*100+fh*500+th*200+thsnd*1000<w:
    print(0)
else:
    if