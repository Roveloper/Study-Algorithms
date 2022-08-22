S = list(map(str, input()))
# print(S)
for i in range(97, 123):
    for j in range(len(S)):
        res = -1
        if chr(i) == S[j]:
            res = j
            break
    print(res, end=' ')