# 08. 07
# 사과문제
N = int(input())

sum = 0

for _ in range(N):
    std, apples = map(int, input().split())
    cnt = apples // std
    sum += apples - (cnt*std)
print(sum)