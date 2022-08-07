# Codeup_4861

# 학생수 n, 최대 인원수 k 입력
n, k = map(int, input().split())

# 각 학년별 학생수 리스트 작성
girl_list = [0 for i in range(6)]
boy_list = [0 for i in range(6)]

for i in range(n):
    s, y = map(int, input().split())
    if s == 0:
        girl_list[y - 1] += 1
    else:
        boy_list[y - 1] += 1

# print(girl_list)
# print(boy_list)
# 여자 방, 남자 방 수를 각각 계산한다.
girl_room = 0
boy_room = 0
cnt_girl = 0
cnt_boy = 0

for i in range(6):
    # 여자 방 개수 계산
    if girl_list[i] <= k:
        if girl_list[i] != 0:
            girl_room += 1
    else:
        cnt_girl = girl_list[i] // k
        if girl_list[i] % k != 0:
            cnt_girl += 1
        girl_room += cnt_girl
    # 남자 방 개수 계산
    if boy_list[i] <= k:
        if boy_list[i] != 0:
            boy_room += 1
    else:
        cnt_boy = boy_list[i] // k
        if boy_list[i] % k != 0:
            cnt_boy += 1
        boy_room += cnt_boy

print(girl_room + boy_room)