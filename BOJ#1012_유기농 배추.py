import sys
sys.setrecursionlimit(100000)

# 상,하,좌,우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x,y):
    graph[x][y] = 0 # 방문
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

# 하나면 visited 필요 # 2차원배열이면 필요없고 0으로바꾸기
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    result = 0
    m,n,k = map(int, sys.stdin.readline().rstrip().split()) # 가로,세로,배추갯수
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        y,x = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1 # 방문 처리
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                result += 1
    print(result)
