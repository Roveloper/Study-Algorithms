N = int(input())
linked = int(input())
network = [[] for _ in range(N + 1)]

for _ in range(linked):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

# print(network)
visited = [False] * (N + 1)


def dfs(network, n, visited):
    visited[n] = True
    for i in network[n]:
        if not visited[i]:
            dfs(network, i, visited)


dfs(network, 1, visited)
# print(visited)
visited[1] = False
# print(visited)
cnt = 0
for i in range(len(visited)):
    if visited[i]:
        cnt += 1
print(cnt)
