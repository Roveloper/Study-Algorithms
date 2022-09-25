# BOJ_1260
from collections import deque
# 입력 넣기
n, m, v = map(int, input().split())


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문 안한 원소들 큐에 넣기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 주어진 각 쌍으로 그래프 만들기
graph = [[] for _ in range(n + 1)] # 1번 인덱스부터 시작
for i in range(m):
    one, two = map(int, input().split())
    graph[one].append(two)
    graph[two].append(one)

for i in range(len(graph)): # n, n + 1 구분하기!!!!
    graph[i].sort()

# print(graph)

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)