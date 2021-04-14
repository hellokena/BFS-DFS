import sys

def dfs(v): # stack, recursion
    visited[v] = 1 # 방문 표시
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1: dfs(i)

def bfs(v): # queue
    queue = [v]
    visited[v] = 1
    while queue:
        v = queue.pop(0) # 맨 앞에꺼
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1

n, m, v = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    from_n, to_n = map(int, sys.stdin.readline().rstrip().split())
    graph[from_n][to_n] = graph[to_n][from_n] = 1
visited = [0] * (n+1)

dfs(v)
visited = [0] * (n+1)  # dfs 후 bfs 초기화
print()
bfs(v)
​
