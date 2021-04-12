import sys

def dfs(x,y):
    global cnt #전역변수 선언
    graph[x][y] = 0 # 방문했다
    cnt += 1 # 단지내의 집 갯수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n: # 움직인 곳이 범위 내의 곳이라면
            if graph[nx][ny]==1: # 이동한곳이 아직 방문하지 않았고 집이 있다면
                dfs(nx,ny)

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

# L, R, U, D
dx = [-1,+1,0,0]
dy = [0,0,-1,+1]

result = []

for i in range(n): # 0,0 부터 시작
    for j in range(n):
        if graph[i][j]==1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)
