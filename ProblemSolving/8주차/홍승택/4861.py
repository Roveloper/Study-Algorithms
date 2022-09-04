#방 배정 문제
# N : 전체 학생 수 / K : 각 방 최대 수용 인원 수
# 학년(1~6)별로 방을 배정해야 하며, 각 학년에서도 남/녀 별로 방을 배정해야함.
# 배정할 방의 수를 최소로 하여 방의 수를 구하기.

ls_boy , ls_girl = [],[]
room = 0
N , K = map(int, input().split()) # 최소한의 방의 수를 구하기 위해선 K로 중복되는 학생 나누기.
for i in range(N):
    S, G = map(int, input().split())
    if S == 0:
        ls_girl.append(G)
    else:
        ls_boy.append(G)
for i in range(1,7):
    a = ls_girl.count(i)
    if a <= K:
        room += 1
    else:
        room += (a/K).ceil
for i in range(1,7):
    b = ls_boy.count(i)
    if a <= K:
        room += 1
    else:
        room += (a/K).ceil
print(room)