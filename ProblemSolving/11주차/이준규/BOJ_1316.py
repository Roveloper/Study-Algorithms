# 09.04 백준 1316 그룹단어체커

N = int(input())

res = 0

for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            res -= 1
            # print(word)
            break
    res += 1
print(res)
