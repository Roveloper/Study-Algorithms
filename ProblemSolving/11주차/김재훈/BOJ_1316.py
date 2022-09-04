# 그룹 단어 찾기
# 그룹 단어 --> 단어에 존재하는 모든 문자에 대해, 각 문자가 연속해서 나타나는 경우
# ccazzzzbb --> c, a, z, b 연속
# kin --> k, i, n이 연속
# aabbbccb --> a, b, c 연속 후 b가 있으므로 연속 아님
# N개의 단어를 입력 받아서, 그룹 단어의 개수를 출력

N = int(input())


# happy
result = 0
for _ in range(N):
    word = input()
    group_word = True
    now = word[0] # h
    unique_char = set(now) # (p)

    for i in word[1:]:
        if now == i:
            pass
        else:
            now = i # now = a
            if now in unique_char: # a의 존재 유무?
                group_word = False
                break
            else:
                unique_char.add(now) # unique_char --> (h, a)
    if group_word:
        result += 1

print(result)


## 1년 전에 풀었던 방식 --> 이게 더 좋아보임
# num = int(input())
# cnt = 0
# for i in range(num):
#     case = input()
#     tmp = 1 # 달라지는 횟수 # happy --> h가 들어올 때 1, a가 들어올 때, 2, p가 들어올때 3, y가 들어올 때 4
#     # aabbcca --> a, 1 --> b, 2 --> c, 3 --> a, 4
#     for i in range(len(case)-1):
#         if case[i+1] == case[i]:
#             pass
#         elif case[i+1] != case[i]:
#             tmp += 1
#     # print(tmp)
#     if tmp == len(set(case)):
#         cnt += 1

# print(cnt)