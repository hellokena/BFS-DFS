import sys
from collections import deque # 최단경로는 bfs로 구현합니다
sys.setrecursionlimit(10000)

h,w = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(h):
    graph.append(list(map(int, str(sys.stdin.readline().rstrip()))))

def bfs(h,w,sh,sw): # 미로 크기(세로 가로), 미로 시작 위치(sh,sw)
    q = deque()
    q.append((sh,sw)) # 0,0 추가
    # 상,하,좌,우
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    while q:
        pop_h,pop_w = q.popleft() # 큐에서 pop
        for i in range(4): # 상하좌우 위치 이동
            nh = pop_h + dh[i]
            nw = pop_w + dw[i]
            #if nh<0 or nh>=h or nw<0 or nw>=w: continue
            #if graph[nh][nw] == 1:
            if 0<=nh<h and 0<=nw<w and graph[nh][nw] == 1:
                graph[nh][nw] = graph[pop_h][pop_w]+1 # 전의 위치에서 +1 해줌
                q.append((nh, nw))
    print(graph[-1][-1]) # 마지막에 저장된 수 출력

bfs(h,w,0,0)
