for _ in range(int(input())):
    n=int(input())
    mydik = {"cakewalk": 0, "easy": 0, "simple": 0, "easy-medium": 0, "medium": 0, "medium-hard": 0, "hard": 0}
    for _ in range(n):
        mydik[input()]+=1
    if mydik["cakewalk"] and mydik["easy"] and mydik["simple"] and (mydik["easy-medium"]+mydik["medium"]) and (mydik["medium-hard"]+mydik["hard"]):
        print("Yes")
    else:
        print("No")