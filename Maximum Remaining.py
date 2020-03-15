_=int(input())
naruto=list(set([int(jiraiya) for jiraiya in input().split()]))
naruto.remove(max(naruto))
if len(naruto)==0:
    print(0)
else:
    print(max(naruto))

#please watch NARUTO ...plssssss ;_;
#"When a man learns to love, he must bear the risk of hatred." - the greatest Uchiha of all times