T = int(input())

for _ in range(T):
    test = input()
    score = 0
    bonus = 1
    for i in range(len(test)):
        if test[i] == 'O':
            score += bonus
            bonus += 1
        elif test[i] == 'X':
            bonus = 1
    print(score)
