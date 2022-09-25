from collections import deque

N, M, V = map(int, input().split())

graphs = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graphs[start].append(end)
    graphs[end].append(start)
    
for i in graphs:
    i.sort()
    
stack = []
Q = deque()
stack.append(V)
Q.append(V)
print(V, end=' ')
visited = [False] * (N + 1)
visited[V] = True

while stack:
    top = stack[-1]
    for i in graphs[top]:
        if visited[i] == False:
            visited[i] = True
            stack.append(i)
            print(i, end=' ')
            break
    else:
        stack.pop()
        
print()
        
visited = [False] * (N + 1)
visited[V] = True

while Q:
    now = Q.popleft()
    print(now, end=' ')
    for i in graphs[now]:
        if visited[i] == False:
            visited[i] = True
            Q.append(i)
            