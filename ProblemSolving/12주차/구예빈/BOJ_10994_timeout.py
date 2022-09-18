# BOJ_10994

# 줄 수 규칙 찾기
# 1 -> 1줄 4 * (1 - 1) + 1
# 2 -> 5줄 4 * (2 - 1) + 1
# 3 -> 9줄 4 * (3 - 1) + 1
# 4 -> 13줄 4 * (4 - 1) + 1

# 각 줄의 규칙 찾기
# 1 : 1
# 2 : 5 2 3 2 5
# 3 : 9 2 ...
# 처음과 끝은 줄 수 만큼 별 넣기


# 값 입력
n = int(input())


# 줄 수를 계산하는 함수
def line_number(n):
    return 4 * (n - 1) + 1


# n에 대해 각 line별로 별을 출력하는 함수를 만든다.
def star_shape(n, line):
    # 1부터 마지막 줄까지 빈칸 저장된 list
    line_shape = ["" for i in range(line_number(n) + 1)]
    if n == 1:
        # line이 1일 때만 있음
        line_shape[1] = "*"
    else: # n이 2이상일 때
        for row in range(1, line_number(n) + 1):
            row_number = line_number(n)
            # 첫번째 줄, 마지막 줄 별모양
            if row == 1 or row == row_number:
                line_shape[row] = "*" * row_number
            # 두번째 줄, 마지막에서 두번째줄 별모양
            elif row == 2 or row == row_number - 1:
                line_shape[row] = '*' + ' ' * (row_number - 2) + '*'
            # 중간에는 이전 라인 보여주기
            else:
                for i in range(1, line_number(n - 1) + 1):
                    line_shape[2 + i] = "* " + star_shape(n - 1, i) + " *"
    return line_shape[line]


# 줄 수 계산
line_Number = 4 * (n - 1) + 1
# 별 찍기
for row in range(1, line_Number + 1):
    print(star_shape(n, row))
