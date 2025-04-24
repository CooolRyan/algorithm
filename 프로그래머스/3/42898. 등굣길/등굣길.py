from collections import deque

def solution(m, n, puddles):
    puddle_set = set((x, y) for x, y in puddles)

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    q = deque()
    q.append((1,1))
    
    
    dp[1][1] = 1
    while q:
        x,y = q.popleft()
        for dx, dy in [(1, 0), (0, 1)]: 
            nx, ny = x + dx, y + dy

            if 1 <= nx <= m and 1 <= ny <= n:
                if (nx, ny) in puddle_set:
                    continue
                if dp[ny][nx] == 0:
                    q.append((nx, ny))
                dp[ny][nx] = (dp[ny][nx] + dp[y][x]) % 1000000007
    # answer = dp[][]%1000000007
                
    return dp[n][m]
    