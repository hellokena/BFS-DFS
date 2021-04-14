import sys

n = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(e):
    from_n, to_n = map(int, sys.stdin.readline().rstrip().split())
    graph[from_n][to_n] = graph[to_n][from_n] = 1

visited = [0]*(n+1)
answer = 0

def dfs(s): #dfs
    global answer
    visited[s] = 1
    #print(s, end= ' ')
    answer += 1
    for i in range(1, n+1):
        if visited[i]==0 and graph[s][i]==1: dfs(i)

dfs(1)
print(answer-1) # 1번 컴퓨터 제외
