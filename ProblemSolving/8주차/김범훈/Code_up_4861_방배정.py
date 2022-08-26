# N : 수학여행 참여학생, K : 한방에 최대 인원수 (K인 1실)
# S : 성별, Y : 학년    
#########
#간단한 풀이
import math
N,K = map(int,input().split())

girl, boy=[] ,[]
sum_girl,sum_boy = 0, 0

for _ in range(0,N):
    S,Y = map(int,input().split())
    if S == 0:
        girl.append(Y)
    if S == 1:
        boy.append(Y)

for i in range(1,7):
    count_girl = math.ceil(girl.count(i)/K)
    sum_girl += count_girl

for i in range(1,7):
    count_boy = math.ceil(boy.count(i)/K)
    sum_boy += count_boy

print(sum_girl+sum_boy)





##복잡한 풀이
# import math
# N,K = map(int,input().split())

# girl=[]
# boy=[]
# count_girl = 0
# count_boy = 0
# sum_girl = 0
# sum_boy = 0
# for _ in range(0,N):
#     S,Y = map(int,input().split())
#     if S == 0:
#         girl.append(Y)
#     if S == 1:
#         boy.append(Y)

# for i in range(1,7):
#     if girl.count(i) == 0:
#         sum_girl += 0
#         continue
#     else:
#         count_girl = math.ceil(girl.count(i)/K)
#         sum_girl += count_girl

# for i in range(1,7):
#     if boy.count(i) == 0:
#         sum_boy += 0
#         continue
#     else:
#         count_boy = math.ceil(boy.count(i)/K)
#         sum_boy += count_boy

# print(sum_girl+sum_boy)

