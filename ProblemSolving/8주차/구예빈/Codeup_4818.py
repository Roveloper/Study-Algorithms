# Codeup_4818

# 2차원 배열 생성
n, m, circle_num = map(int, input().split())
path_list = [[0 for j in range(m)] for i in range(n)]
num = 1
for i in range(n):
    for j in range(m):
        path_list[i][j] = num
        num += 1
# print(path_list)



# 중학교 수열 길찾기 수학 문제로 풀어본다.
# 동그라미 친 숫자가 없을 때
#전체 2차원 배열의 최단 경로를 구해본다.
def short_calculate(n, m):
    short_list = [[1 for j in range(m)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            short_list[i][j] = short_list[i - 1][j] + short_list[i][j - 1]
    return (short_list[n - 1][m - 1])

# 동그라미 친 숫자가 없을 때
if circle_num == 0:
    answer = short_calculate(n, m)
    print(answer)

else:
    # 동그라민 친 숫자의 인덱스를 구해본다.
    for i in range(n):
        for j in range(m):
            if path_list[i][j] == circle_num:
                circle_x = i
                circle_y = j
            else:
                continue
    # print(circle_x, circle_y)


    # 동그라미 숫자를 거치는 최단 경로를 구해본다.
    short1 = short_calculate(circle_x + 1, circle_y + 1)
    short2 = short_calculate(n - circle_x, m - circle_y)
    answer = short1 * short2
    print(answer)




