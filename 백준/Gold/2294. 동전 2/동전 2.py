n, result = map(int, input().split())
arr = []
for _ in range(n):
    temp = int(input())
    if temp not in arr:
        arr.append(temp)
INF = 10**9
dp = [INF] * (result + 1)
dp[0] = 0
for i in arr:
    for j in range(i, result+1):
        dp[j] = min(dp[j], dp[j-i] + 1)

if dp[result] == INF:
    print(-1)
else:
    print(dp[result])