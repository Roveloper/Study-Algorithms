# 08.07
N = int(input())
score = list(map(int,input().split()))
print(max(score)-min(score))