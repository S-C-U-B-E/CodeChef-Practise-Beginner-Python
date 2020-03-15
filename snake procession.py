for _ in range(int(input())):
    l=int(input())
    s=input().upper()
    s=s.replace('.','')
    print("Valid"*bool(2*s.count("HT")==len(s))+"Invalid"*bool(2*s.count("HT")!=len(s)))
