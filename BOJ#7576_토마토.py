import sys
from collections import deque # 최단경로는 bfs로 구현합니다
sys.setrecursionlimit(10000)

def bfs(h,w,graph):
    # 상,하,좌,우
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    q = deque()
    # 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
    time = -1 # 처음 토마토는 주어질때부터 익어있었으므로 시간이 0으로 되야함
    for i in range(h): # 익은 토마토가 있으면 queue에 추가
        for j in range(w):
            if graph[i][j] == 1:
                q.append((i,j))
    while q:
        time += 1
        for _ in range(len(q)): # ** 한번에 넣은 토마토는 한번에 접근함
            pop_h,pop_w = q.popleft() # 큐에서 pop
            for i in range(4): # 상하좌우 위치 이동
                nh = pop_h + dh[i]
                nw = pop_w + dw[i]
                # 주위의 토마토가 익지 않았을 경우
                if 0<=nh<h and 0<=nw<w and graph[nh][nw] == 0:
                    graph[nh][nw] = 1 # 익게 만듬
                    q.append((nh, nw))
    return time

def solution():
    w, h = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    time = bfs(h,w,graph)

    checker = True

    for i in graph:
        if 0 in i:
            checker = False
            print(-1)
            break

    if checker:
        print(time)

solution()
