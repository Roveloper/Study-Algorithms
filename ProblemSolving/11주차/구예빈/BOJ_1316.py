# BOJ_1316

# 그룹단어 갯수
n = int(input())
group_number = 0

for i in range(n):
    words = list(map(str, input()))

group
    # 단어의 중복을 없앤 후에
    words_set = set(words)
    words_list = list(words_set)
    tmp = words[0]
    for word in words_list:
        for j in range(len(words)):
            if words[j] != tmp:
                if words_list.count(tmp) > 0:
                    words_list.pop()
                else:
                    break
            tmp = words[j]
    group_number += 1
    print(group_number)




