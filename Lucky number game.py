t=int(input())


for q in range(t):
    A = []
    bob = alice = True
    inputs=list(map(int,input().strip().split()))
    n=inputs[0]
    a=inputs[1]
    b=inputs[2]

    for x in range(n):
        A.append(int(input()))

    while bob and alice:
        c=0
        bob=False
        alice=False
        for i in A:
            if i%a==0:
                A.remove(i)
                bob=True
                c+=1

        if bob:
            for x in range(c):
                for i in A:
                    if i%b==0:
                      A.remove(i)
                      alice=True
                      break
                if not alice:
                    break
            #if not alice:
            #    print("BOB")
            #   break
        #else:
        #    print("ALICE")
        #    break

    if not bob:
        print("ALICE")
    else:
        print("BOB")



