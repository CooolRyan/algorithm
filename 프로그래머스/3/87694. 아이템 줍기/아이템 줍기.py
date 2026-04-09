from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 102
    board = [[0] * MAX for _ in range(MAX)]

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    start_x, start_y = characterX * 2, characterY * 2
    target_x, target_y = itemX * 2, itemY * 2

    visited = [[False] * MAX for _ in range(MAX)]
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, dist = q.popleft()

        if x == target_x and y == target_y:
            return dist // 2

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < MAX and 0 <= ny < MAX:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))