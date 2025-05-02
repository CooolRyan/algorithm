from collections import deque
pos, dest = map(int, input().split())

q = deque()
time = [float('inf')] * 1000001
time[pos] = 0
q.append(pos)

while q:
    cur = q.popleft()

    for npos, ntime in ((cur * 2, 0), (cur - 1, 1), (cur + 1, 1)):
        if 0 <= npos <= 1000000:
            if time[npos] > time[cur] + ntime:
                time[npos] = time[cur] + ntime
                if ntime == 0:
                    q.appendleft(npos)
                else:
                    q.append(npos)

print(time[dest])