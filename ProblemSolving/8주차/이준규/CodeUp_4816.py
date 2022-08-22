# 08.07
# 전자레인지
# 시간 조절 버튼 3개 : A = 5분 300 초 , B = 1분 = 60초, C = 10초
# 냉동음식 조리필요시간 T초 -> A + B + C = T
# A + B + C 최소값

T = int(input())

A = 300
B = 60
C = 10

A_res = T // 300
B_res = (T % 300) // 60
C_res = ((T % 300) % 60) // 10
check = ((T % 300) % 60) % 10

if check == 0:
    print(A_res, B_res, C_res)
else:
    print(-1)
