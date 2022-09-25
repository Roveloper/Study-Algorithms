# BOJ_2606

# 컴퓨터의 수와 쌍의 수 입력
n = int(input())
m = int(input())
global visit_node
visit_node = []


# 인접한 노드로 연결된 노드 덩어리를 추출 > dfs 로 구현
def dfs(graph, v, visited):
    global visit_node
    # 현재 노드를 방문 처리
    visited[v] = True
    visit_node.append(v)
    # 현재 노드와 연결된 다른 노드를 재귀로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 주어진 각 쌍으로 그래프 만들기
graph = [[] for _ in range(n + 1)] # 1번 인덱스부터 시작
# graph = [[] * (n + 1)] # 이거 안됨
# graph = [[], [], [], [], [], [], [], []] # 이거 됨
for i in range(m):
    one, two = map(int, input().split())
    graph[one].append(two)
    graph[two].append(one)


# 각 노드가 방문된 정보를 리스트로 저장
visited = [False] * (n + 1) # 여기 주의!! n 아님 - 런타임 에러(index error) 뜸

dfs(graph, 1, visited)
# 방문한 노드들을 저장한 리스트의 길이에서 하나를 뺀다.
print(len(visit_node) - 1)
