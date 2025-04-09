from collections import deque

def solution(n, edge):
    answer = 0
    visit = [False for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque()
    queue.append(1)
    visit[1] = True
    
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visit[next]:
                visit[next] = True
                dist[next] = dist[now] + 1
                queue.append(next)

    m = max(dist)
    print(dist)
    return dist.count(m)

    