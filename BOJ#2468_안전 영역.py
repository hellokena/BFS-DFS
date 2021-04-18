#DFS # 유기농배추랑 비슷
import sys
sys.setrecursionlimit(100000)

# 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def dfs(hindex, windex, heightidx):
    
    visited[hindex][windex] = 1 # 방문처리
    
    for i in range(4):
        nh = hindex + dh[i]
        nw = windex + dw[i]
        
        if 0<=nh<n and 0<=nw<n and graph[nh][nw] > heightidx and visited[nh][nw] == 0: # 안전지대일 경우 순회
            dfs(nh, nw, heightidx)

# main
n = int(sys.stdin.readline().rstrip()) # N*N 그래프
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    
result = 0

# 비가 오는 양을 1 ~ 배열 내 최댓값까지
for height in range(max(map(max, graph))): 
    # 각 높이마다 방문 그래프 초기화
    visited = [[0]*n for _ in range(n)]
    safe = 0 # 안전지대
    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and visited[i][j] == 0: # 안전지대이면
                dfs(i,j, height)
                safe += 1
        result = max(result, safe)

print(result)
