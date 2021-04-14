import sys
sys.setrecursionlimit(10000)

# 북서,북,북동,동,동남,남,남서,서
dh = [-1, -1, -1, 0, 1, 1, 1, 0]
dw = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(h_idx,w_idx):
    graph[h_idx][w_idx] = 0 # 방문처리
    for i in range(8):
        nh = h_idx + dh[i]
        nw = w_idx + dw[i]
        #if nh < 0 or nh >= h or nw < 0 or nw >= w: continue
        #if graph[nh][nw] == 1:
            #dfs(nh, nw)
        if 0<=nh<h and 0<=nw<w:
            if graph[nh][nw] == 1: dfs(nh,nw)

while True:
    w,h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0: break
    graph = []
    cnt = 0
    # graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(h)]
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)
