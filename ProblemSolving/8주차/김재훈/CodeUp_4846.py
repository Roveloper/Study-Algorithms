# 학생들에게 나눠주고 남는 사과의 총 개수를 구하는 프로그램 작성

N = int(input())

remainder = 0

for _ in range(N):
    A, B = map(int, input().split())

    remainder += B % A

print(remainder)