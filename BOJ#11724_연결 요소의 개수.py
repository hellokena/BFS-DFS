import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    from_n, to_n = map(int, sys.stdin.readline().rstrip().split())
    graph[from_n][to_n] = graph[to_n][from_n] = 1
visited =[0]*(n+1)
cnt = 0

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1: dfs(i)

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
