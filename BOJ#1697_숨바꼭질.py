import sys
from collections import deque # 최단경로는 bfs로 구현합니다
sys.setrecursionlimit(10000)

def bfs(from_n, to_n, move):
    q = deque()
    q.append(from_n) # 시작점 append

    while q:
       v = q.popleft()
       if v == to_n: # 수빈이가 동생의 위치에 도달했을 때
           print(move[v]) # 이동한거리=걸린 시간 출력
           return
       for next_p in [v-1, v+1, v*2]:
           if 0<=next_p<=100000 and move[next_p]==0:
                move[next_p] = move[v] + 1
                q.append(next_p)

def solution():
    from_n,to_n = map(int, sys.stdin.readline().rstrip().split())
    move = [0]*100001 #0~100,000은 100001임
    bfs(from_n, to_n, move)

solution()
