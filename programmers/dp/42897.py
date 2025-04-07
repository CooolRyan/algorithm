def solution(money):
    answer = 0
    dp0 = [0 for _ in range(len(money) - 1)]
    dp1 = [0 for _ in range(len(money) - 1)]
    dp0[0] = money[0]
    dp0[1] = max(money[0],money[1])
    dp1[0] = money[1]
    dp1[1] = max(money[1],money[2])
    
    for i in range(2 ,len(money) - 1):
        dp0[i] = max(dp0[i-1], dp0[i-2] + money[i])    
    for i in range(2 ,len(money) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i+1])    
    return max(max(dp0),max(dp1))