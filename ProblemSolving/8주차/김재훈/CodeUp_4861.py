# 최대 인원 K
# 조건에 맞게 학생을 배정하기 위한 방의 최소 개수를 구하는 프로그램

# 한 방에는 같은 학년의 학생을 배정해야하며
# 남자는 남자끼리, 여자는 여자끼리 배정해야함

# K인 1실 기준 (1인 1실도 가능)

N, K = map(int, input().split())

rooms = [0] * 12 # 1학년 ~ 6학년 여, 1 ~ 6학년 남 순서로 배치
entire_room_cnt = 0
for _ in range(N):
    S, Y = map(int, input().split())
    room_number = S * 6 + (Y - 1) # 1학년 여자 --> 0, 1학년 남자 --> 6, 5학년 여자 --> 4, 5학년 남자 --> 10
    if rooms[room_number] == 0:
        entire_room_cnt += 1
        rooms[room_number] += 1

    else:
        rooms[room_number] += 1

    if rooms[room_number] == K:
        rooms[room_number] = 0

print(entire_room_cnt)
