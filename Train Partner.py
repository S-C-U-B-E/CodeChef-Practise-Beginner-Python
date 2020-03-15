for _ in range(int(input())):
    n=int(input())
    dic = {3: "UB", 2: "MB", 1: "LB", 7: "SU", 6: "UB", 5: "MB", 4: "LB", 0: "SL"}
    dik = {3: 6, 2: 5, 1: 4, 7: 8, 6: 3, 5: 2, 4: 1, 0: -1}
    print(8*(n//8)+dik[n%8],dic[n%8],sep='')