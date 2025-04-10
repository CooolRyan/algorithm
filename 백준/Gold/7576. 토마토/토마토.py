from collections import deque

row, col = map(int, input().split())

dx = [0, 0, -1, 1]  # 좌 우 상 하
dy = [-1, 1, 0, 0]
tomato = [[0 for _ in range(row)] for _ in range(col)]
for i in range(col):
    temp = list(map(int,input().split()))
    tomato[i] = temp
q = deque()

days = [[0 for _ in range(row)] for _ in range(col)]

for i in range(col):
    for j in range(row):
        if tomato[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < col and 0 <= ny < row:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                days[nx][ny] = days[x][y] + 1
                q.append((nx, ny))

result = 0
for i in range(col):
    for j in range(row):
        if tomato[i][j] == 0:  # 아직도 안 익은 애가 있다면
            print(-1)
            exit()
        result = max(result, days[i][j])
print(result)