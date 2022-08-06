# BOJ_2578

n = 5
# 철수의 빙고판 2차원 배열 입력한다.
plate = [list(map(int, input().split())) for _ in range(n)]
# 사회자 부르는 값 입력
host = [list(map(int, input().split())) for _ in range(n)]

# 12개의 경우를 담은 빙고 리스트와 사회자가 숫자를 부른 횟수
bingo = list(0 for i in range(n + n + 2))
print(bingo)
bingo_cnt = 0
cnt = 0

# 사회자가 부른 숫자를 빙고판에서 0으로 바꾼다.
for x_ in range(n):
    for y_ in range(n):
        cnt += 1
        host_number = host[x_][y_]
        print(cnt, host_number)
        for x in range(n):
            for y in range(n):
                if plate[x][y] == host_number:
                    plate[x][y] = 0
        for i in range(n):
            if plate[i][0] == 0 and plate[i][1] == 0 and plate[i][2] == 0 and plate[i][3] == 0 and plate[i][4] == 0:
                bingo[i] = 1
                for k in range(len(bingo)):
                    bingo_cnt += bingo[k]
                if bingo_cnt >= 3:
                    print(cnt)
                    bingo_cnt = 100
                    break
            if plate[0][i] == 0 and plate[1][i] == 0 and plate[2][i] == 0 and plate[3][i] == 0 and plate[4][i] == 0:
                bingo[i + 5] = 1
                for k in range(len(bingo)):
                    bingo_cnt += bingo[k]
                if bingo_cnt >= 3:
                    print(cnt)
                    bingo_cnt = 100
                    break
            if plate[0][0] == 0 and plate[1][1] == 0 and plate[2][2] == 0 and plate[3][3] == 0 and plate[4][4] == 0:
                bingo[10] = 1
                for k in range(len(bingo)):
                    bingo_cnt += bingo[k]
                if bingo_cnt >= 3:
                    print(cnt)
                    bingo_cnt = 100
                    break

            if plate[0][4] == 0 and plate[1][3] == 0 and plate[2][2] == 0 and plate[3][1] == 0 and plate[4][0] == 0:
                bingo[11] = 1
                for k in range(len(bingo)):
                    bingo_cnt += bingo[k]
                if bingo_cnt >= 3:
                    print(cnt)
                    bingo_cnt = 100
                    break
            print(bingo)
        if bingo_cnt == 100:
            break