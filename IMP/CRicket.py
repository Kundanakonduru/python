def ScoreBoard(overs,run=0,wickets=1):
    l=[]
    for i in range(overs):
        print(f"{i+1} over:")
        ball=1
        while ball<=6:
            print(f"{ball}ball:")
            if wickets>0 and wickets<=10:
                score=input().lower()
                if score=="wd"or score=="nd":
                    l.append(score)
                    run+=1
                elif score=="w":
                    l.append(score)
                    wickets+=1
                    ball+=1
                else:
                    if int(score) in range(1,8):
                        l.append(score)
                        run+=int(score)
                        ball+=1
            else:
                break
            
    print(l)
    print(run)
    print(wickets)
                    
            
        
        
ScoreBoard(2)
