# 행의 개수가 N
# 열의 개수가 M
# 1부터 N X M까지 있음
# 격자의 어떤 칸은 O표시가 되어 있음
# 1번칸과 N X M칸은 O표시가 되어 있지 않음
# O표시가 되어 있는 칸은 최대 1개 (없을 수도 있다는 뜻)

# 1번 칸에서 로봇이 출발
# N X M 번 칸으로 가고자 함

# 조건1. 로봇은 한 번에 오른쪽 또는 아래쪽으로 한칸 이동 가능 (대각선 X)
# 조건2. O가 표시된 칸이 있는 경우, 그 칸을 꼭 지나가야 함

def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)

N, M, K = map(int, input().split())


if K == 0:
    down_num = N - 1
    right_num = M - 1

    method_num = factorial(down_num + right_num) / (factorial(down_num) * factorial(right_num))

else:
    X, Y = divmod(K, M) # 1, 3

    # down_num = X

    if Y == 0:
        right_num = M - 1
        down_num = X - 1

    else:
        right_num = Y - 1
        down_num = X

    down_num2 = N - 1 - down_num
    right_num2 = M - 1 - right_num

    before_method = factorial(down_num + right_num) / (factorial(down_num) * factorial(right_num))

    after_method = factorial(down_num2 + right_num2) / (factorial(down_num2) * factorial(right_num2))


    method_num = before_method * after_method

print(int(method_num))

# 01 02 03 04 05 06 07 08 09 10 11 12 13 14
# 15 16 17 18 19 20 21 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36 37 38 39 40 41 42
# 43 44 45 46 47 48 49 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64 65 66 67 68 69 70
# 71 72 73 74 75 76 77 78 79 80 81 82 83 84
# 85 86 87 88 89 90 91 92 93 94 95 96 97 98

# 7 14 70