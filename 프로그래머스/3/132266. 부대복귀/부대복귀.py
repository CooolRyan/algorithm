from collections import deque

def solution(n, roads, sources, destination):
    q = deque()
    
    answer = []
    vertex = [[] for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    for a,b in roads:
        vertex[a].append(b)
        vertex[b].append(a)
        
    dist[destination] = 0
    visited[destination] = True
    
    q.append([destination, 0])
    while q:
        node, cnt = q.popleft()
        for i in vertex[node]:
            if not visited[i]:
                visited[i] = True
                dist[i] = cnt + 1
                q.append([i, cnt + 1])
    for i in sources:
        answer.append(dist[i])
        
    return answer