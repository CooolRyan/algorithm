import heapq
def solution(n, s, a, b, fares):    
    graph = [[] for _ in range(n+1)]
    for i,j,k in fares:
        graph[i].append((j,k))
        graph[j].append((i,k))
        
        
    
    heap = []
    dists = [float('inf') for _ in range(n+1)]
    dista = [float('inf') for _ in range(n+1)]
    distb = [float('inf') for _ in range(n+1)]

    dists[s] = 0
    dista[a] = 0
    distb[b] = 0
    
    heapq.heappush(heap,(0,s))
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > dists[node] :
            continue
            
        for v, w in graph[node]:
            new = cost + w
            if new < dists[v]:
                dists[v] = new
                heapq.heappush(heap,(new, v))
            
    heap=[]
    heapq.heappush(heap,(0,a))
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > dista[node] :
            continue
            
        for v, w in graph[node]:
            new = cost + w
            if new < dista[v]:
                dista[v] = new
                heapq.heappush(heap,(new, v))

                
    heap=[]
    heapq.heappush(heap,(0,b))
    while heap:
        cost, node = heapq.heappop(heap)
        
        if cost > distb[node] :
            continue
            
        for v, w in graph[node]:
            new = cost + w
            if new < distb[v]:
                distb[v] = new
                heapq.heappush(heap,(new, v))

                
    answer = float('inf')
    for k in range(1, n+1):
        answer = min(answer, dists[k] + dista[k] + distb[k])

    print(dista)
    print(dists)
    print(distb)
    
    return answer

