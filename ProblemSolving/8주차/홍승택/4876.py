#딱지놀이 문제
# A B 두 학생이 대결 . 별, 동그라미, 네모, 세모 - 각각 4,3,2,1 의 숫자로 표현
# (카드의 도형 갯수) , (각 도형에 해당하는 숫자 나열) 로 표현 -> EX, A : 1 , 4 == 1개 , 별.

N = int(input())

for i in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.pop(0)
    B.pop(0)

    A_star = A.count(4)
    B_star = B.count(4)
    A_circle = A.count(3)
    B_circle = B.count(3)
    A_square = A.count(2)
    B_square = B.count(2)
    A_triangle = A.count(1)
    B_triangle = B.count(1)

    if A_star > B_star:
        print('A')
    elif A_star < B_star:
        print('B')
    elif A_circle > B_circle:
        print('A')
    elif A_circle < B_circle:
        print('B')
    elif A_square > B_square:
        print('A')
    elif A_square < B_square:
        print('B')
    elif A_triangle > B_triangle:
        print('A')
    elif A_triangle < B_triangle:
        print('B')
    else:
        print('D')
