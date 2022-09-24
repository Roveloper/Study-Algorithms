# BOJ_10994

# 이전 코드가 timeout 되었으므로 다른 방식으로 접근하도록 한다.
# 직사각형 만들어나가기

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
length = 4 * (n - 1) + 1

# 별들을 저장하는 2차원 배열 만들기
stars = [[" "] * length for i in range(length)]

# 바깥쪽부터 직사각형 그리기
# 직사각형 갯수는 n개
for i in range(1, n + 1):
    # 각 직사각형 길이, 시작, 끝 인덱스를 계산한다.
    square_length = 4 * (i - 1) + 1
    start = 2 * (n - i)
    end = start + square_length
    # 직사각형 범위
    for row in range(start, end):
        for col in range(start, end):
            # 맨 아래, 위는 별로 모두 채우기
            if row == start or row == end - 1:
                stars[row][col] = "*"
            # 가운데는 양쪽 끝단만 별로 채우기
            else:
                if col == start or col == end - 1:
                    stars[row][col] = "*"
                else:
                    continue


# 별을 출력해준다.
for i in range(length):
    print(''.join(stars[i]))

