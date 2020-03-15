import calendar as cal
for _ in range(int(input())):
    n=int(input())
    dic={0: "monday", 1: "tuesday", 2: "wednesday", 3: "thursday", 4: "friday", 5: "saturday", 6: "sunday"}
    print(dic[cal.weekday(n,1,1)])