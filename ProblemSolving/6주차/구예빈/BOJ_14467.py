# 14467 소가 길을 건너간 이유1

# 관찰 횟수 n
n = int(input())

# 1-10번 소의 위치를 저장한 배열: 0,1이 아닌 2로 저장해둔다.
cow = list(2 for i in range(0, 11))

# 위치가 바뀐 횟수 계산하기
cnt = 0
for i in range(n):
    cow_num, cow_pos = map(int, input().split())

    if cow_pos == cow[cow_num]:
        continue
    elif cow[cow_num] != 2 or cow_pos != cow[cow_num]:
        cnt = cnt + 1
        cow[cow_num] = cow_pos

print(cnt)




