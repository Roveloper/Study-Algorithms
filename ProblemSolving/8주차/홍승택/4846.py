#사과 문제
# 사과 나눠주기 : (전체 사과) -> 학교 A,B,C,.. 로 -> 각 학교의 학생수로.
# 남는 사과 갯수가 최소가 되게끔.
# N : 학교 수. N 개의 줄마다 각 학교 학생 수 및 배정된 사과 갯수 주어짐(정수)

rest_apple = []
sum_ra = 0
N = int(input())
for i in range(N):
    students_number, apple_quantity = map(int, input().split())
    a,b = divmod(apple_quantity,students_number)
    rest_apple = b
    sum_ra = sum_ra + b
print(sum_ra)