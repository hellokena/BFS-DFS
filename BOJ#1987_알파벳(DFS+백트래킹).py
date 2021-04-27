import sys
sys.setrecursionlimit(100000)
height, width = map(int, sys.stdin.readline().rstrip().split())
graph = []
#상하좌우
dh = [1, -1, 0, 0]
dw = [0, 0, -1, 1]
graph = [list(sys.stdin.readline().rstrip()) for _ in range(height)]
visited = [0]*26

def dfs(hidx, widx, cnt):
    visited[ord(graph[hidx][widx])-65] = 1 # 방문처리
    global result
    result = max(result,cnt)
    for i in range(4):
        nh = hidx + dh[i]
        nw = widx + dw[i]
        if 0<=nh<height and 0<=nw<width:
            if visited[ord(graph[nh][nw])-65] == 0:
                dfs(nh, nw, cnt+1)
                visited[ord(graph[nh][nw])-65] = 0 # 백트래킹

#for i in range(height):
#    for j in range(width):
#        if graph[i][j] not in move:
#            dfs(i,j)
result = 1
dfs(0,0,result)
print(result)
#if __name__ == '__main__':


