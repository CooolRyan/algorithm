length = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(length)]
    
for i in range(1,length):
    idx = i - 1
    max_val = 0
    while idx > -1:
        if arr[idx] < arr[i]:
            max_val = max(max_val, dp[idx])
        idx -= 1
    dp[i] = max_val + 1
print(max(dp))