def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, i, visited)
            answer += 1
    return answer

# [PRG] 매개변수로 computers와 visited도 넘겨주어야함
def dfs(n, computers, v, visited): 
    visited[v] = 1 # 방문 확인
    for i in range(n):
        if visited[i] == 0 and computers[v][i] == 1:
            dfs(n, computers, i, visited)
