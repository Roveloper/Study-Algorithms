from collections import deque
N, M, V = map(int, input().split())

network = [[] for _ in range(N + 1)]
link_list = []
link_list2 = []
visited_D = [False] * (N + 1)
visited_B = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

for i in range(len(network)):
    network[i].sort()


def dfs(graph, v, visit):
    # 현재 노드를 방문 처리
    visit[v] = True
    link_list.append(v)
    for i in graph[v]:
        if not visit[i]:
            dfs(graph, i, visit)


def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        v = queue.popleft()
        link_list2.append(v)

        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


dfs(network, V, visited_D)
bfs(network, V, visited_B)
print(*link_list)
print(*link_list2)
