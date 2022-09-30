def DFS(lst,v,visited):
  visited[v] = True

  for node in lst[v]:
    # print(node)
    if not visited[node]:
      
      DFS(lst, node, visited)

  return visited


com_num = int(input(''))
link = int(input(''))

network = [[]*(com_num+1) for _ in range(com_num+1)]

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

com=[False] * (com_num+1)
visit=DFS(network,1,com)

print(visit.count(True)-1)
