# OX 퀴즈 문제

N = int(input())
for _ in range(N):
    S = input()
    total_score = 0
    score = 0
    for i in S:
        if i == 'X':
            score = 0
        else:
            score += 1
        total_score += score

    print(total_score)