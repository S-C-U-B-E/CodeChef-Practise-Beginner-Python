for _ in range(int(input())):
    c=input()
    print("BattleShip"*bool(c=='B' or c=='b')+"Cruiser"*bool(c=='C' or c=='c')+"Destroyer"*bool(c=='D' or c=='d')+"Frigate"*bool(c=='F' or c=='f'))