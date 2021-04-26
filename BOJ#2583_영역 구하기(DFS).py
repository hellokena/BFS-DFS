# dfs
import sys
sys.setrecursionlimit(100000)
height,width,k = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*width for _ in range(height)]
# 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]
resultarray = []
for i in range(k):
    leftw, lefth, rightw, righth = map(int, sys.stdin.readline().rstrip().split())
    for h in range(lefth, righth):
        for w in range(leftw, rightw):
            graph[h][w] = 1

cnt = 0
result = 0
def dfs(hidx, widx):
    global cnt
    global result
    graph[hidx][widx] = 1 #방문처리
    result += 1 # 각 영역의 넓이
    for i in range(4):
        nh = hidx + dh[i]
        nw = widx + dw[i]
        if 0<=nh<height and 0<=nw<width and graph[nh][nw] == 0:
            dfs(nh, nw)

for i in range(height):
    for j in range(width):
        if graph[i][j]==0:
            dfs(i,j)
            cnt += 1 # 빈 영역 갯수
            resultarray.append(result)
            result = 0

print(cnt)
resultarray.sort()
for result in resultarray:
    print(result, end = ' ')
