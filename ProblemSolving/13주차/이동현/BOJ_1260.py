from collections import deque

def bfs(lst,start,visited):
  visited[start] = True
  queue = [starting]
  while queue:
    for node in lst[queue.pop()]:
      if not visited[node]:
        visited[node]=True
        queue.insert(0,node)
        print(node,end=' ')

def dfs(lst,v,visited):
  visited[v] = True

  for node in lst[v]:
    
    if not visited[node]:
      print(node,end=' ')
      dfs(lst, node, visited)


point, line, starting = map(int, input('').split())

lst= [[] for _ in range(point+1)]
for i in range(line):
  a,b = map(int, input().split())
  lst[a].append(b)
  lst[b].append(a)

for i in range(len(lst)):
  lst[i].sort()

visited_dfs = [False]*(point+1)
print(starting,end = ' ')
dfs(lst, starting, visited_dfs)

print()
visited_bfs = [False]*(point+1)
print(starting,end = ' ')
bfs(lst, starting, visited_bfs)
