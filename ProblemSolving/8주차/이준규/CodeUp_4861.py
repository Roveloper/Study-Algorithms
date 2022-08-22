# 08.07
# N = 참가하는 학생수
# K = 방의 최대인원수
# 각줄에는 S 성별 (남 :1, 여 0 ), Y 학년
import math
boys, girls = [] , []
boys_room, girls_room = 0, 0

N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 1:
        boys.append(Y)
    else:
        girls.append(Y)
# print(boys, girls)
for i in range(1, 7):
    if boys.count(i) == 0:
        boys_room += 0
        continue
    else:
        boys_cnt = math.ceil(boys.count(i) / K)
        boys_room += boys_cnt
for j in range(1, 7):
    if girls.count(j) == 0:
        girls_room += 0
        continue
    else:
        girls_cnt = math.ceil(girls.count(j) / K)
        girls_room += girls_cnt

print(boys_room+girls_room)
