length = int(input())

level = []
for _ in range(length):
    a = int(input())
    level.append(a)
dp = [0 for _ in range(length)]
if length == 1:
    print(level[0])
    exit()
elif length == 2:
    print(level[0] + level[1])
    exit()

dp[0] = level[0]
dp[1] = level[0] + level[1]
dp[2] = max(dp[0] + level[2], level[1] + level[2])

for n in range(3, len(dp)):
    dp[n] = max(dp[n-2]+level[n], dp[n-3] + level[n-1] + level[n])

print(dp[-1])
