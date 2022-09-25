# 1번 컴퓨터로부터 영향을 받아서 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력
from collections import deque

# DFS --> Tree 구조 찾을 때 더 많이 쓰는 거 같아요, 끝까지 갔다가 돌아오는 구조
# BFS --> 최단거리 계산을 빨리해야할 때, 시작점을 중심으로 넓어지는 구조, 경로 탐색 시 유리

N = int(input())

graphs = [[] for _ in range(N + 1)] # list() --> 새로운 주소에 할당
for _ in range(int(input())):
    start, target = map(int, input().split())
    graphs[start].append(target) # 시작 --> 도착
    graphs[target].append(start) # 도착 --> 시작
    
## DFS든 BFS든 암튼 총 몇대인지 찾기만 하면 됨
def DFS():
    global cnt
    while stack:
        top = stack[-1] # stack에 제일 위에 있는 값
        for i in graphs[top]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
                cnt += 1
                break
        else:
            stack.pop()

cnt = 0
stack = [1]
visited = [False] * (N + 1)
visited[1] = True
DFS()
print(cnt)


# ## BFS로 찾아보자

# cnt = 0
# Q = deque([1])
# visited = [False] * (N + 1)
# visited[1] = True

# while Q:
#     now = Q.popleft()
#     for i in graphs[now]:
#         if visited[i] == False:
#             visited[i] = True
#             # print(i)
#             Q.append(i)
#             cnt += 1           
# print(cnt)