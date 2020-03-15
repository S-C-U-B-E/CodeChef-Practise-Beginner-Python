for _ in range(int(input())):
    s1=[x for x in input().split()]
    s2=[x for x in input().split()]
    if len(set.intersection(set(s1),set(s2)))>=2:
        print("similar")
    else:
        print("dissimilar")