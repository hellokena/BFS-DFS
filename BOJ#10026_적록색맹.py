import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline().rstrip())

# 정상인 그래프
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
normal = 0
disease = 0

def dfs(hidx, widx):
    global normal
    global disease
    visited[hidx][widx] = 1 # 방문처리
    for i in range(4):
        nh = hidx + dh[i]
        nw = widx + dw[i]
        if 0<=nh<n and 0<=nw<n:
            if graph[nh][nw] == graph[hidx][widx] and visited[nh][nw] == 0: # 같은 영역
                dfs(nh, nw)

# 정상인
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            normal += 1 # 영역 갯수
            
# 적록색맹 그래프
for i in range(n): # 그래프 변경
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 적록색맹
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            disease += 1 # 영역 갯수

print(normal, disease)



