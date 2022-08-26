################
number = int(input(""))

for i in range(0,number):
    score = 0
    score_all = 0
    OX=input("")
    for j in list(OX):
        if j == 'O':
            score+=1
            score_all += score
        else:
            score=0
    print(score_all)