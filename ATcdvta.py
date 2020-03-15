n=int(input())
w=int(input())
h=int(input())
th=int(input())
fh=int(input())
thsnd=int(input())

fin,ini=0,0

nthsnd = int(w/1000)
nfh = int((w-nthsnd*1000)/500)
nth = int((w-nthsnd*1000-nfh*500)/200)
nh = int((w-nthsnd*1000-nfh*500-nth*200)/100)
'print(nthsnd+nfh+nth+nh,nthsnd,nfh,nth,nh)'
'i=0'
if w>(h*100+th*200+fh*500+thsnd*1000):
    print(0)
elif n<(nthsnd+nfh+nth+nh) or h<nh or th<nth or fh<nfh or thsnd<nthsnd:
    print(0)
elif n==(nthsnd+nfh+nth+nh) and (nh<=h and nth<=th and nfh<=fh and nthsnd<=thsnd):
    print(n)
else:
    while True:
        'i+=1'
        ini = nthsnd+nfh+nth+nh

        while 10+nh<=h and nthsnd>0 and (nthsnd-1)+nfh+nth+(nh+10)<=n:
            nthsnd=nthsnd-1
            nh=nh+10
        while 5+nh<=h and nfh>0 and nthsnd+(nfh-1)+nth+(5+nh)<=n:
            nfh=nfh-1
            nh=nh+5
        while 2+nh<=h and nth>0 and nthsnd+nfh+nth-1+nh+2<=n:
            nth=nth-1
            nh=nh+2
        'print("i=" + str(i), nthsnd, nfh, nth, nh)'

        while 5+nth<=th and nthsnd>0 and nthsnd-1+nfh+nth+5+nh<=n:
            nthsnd=nthsnd-1
            nth=nth+5
        while 2+nth<=th and 1+nh<=h and nfh>0 and nthsnd+nfh-1+nth+2+nh+1<=n:
            nfh=nfh-1
            nh=nh+1
            nth=nth+2
        'print("i=" + str(i), nthsnd, nfh, nth, nh)'

        while 2+nfh<=fh and nthsnd>0 and nthsnd-1+nfh+2+nth+nh<=n:
            nthsnd=nthsnd-1
            nfh=nfh+2

        'print("i="+str(i),nthsnd,nfh,nth,nh)'
        fin = nthsnd+nfh+nth+nh
        if fin==ini:
            break


    if fin<=n:
        print(fin)
    else:
        print(0)






