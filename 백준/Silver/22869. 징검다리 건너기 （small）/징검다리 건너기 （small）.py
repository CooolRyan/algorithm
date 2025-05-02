num, power = map(int, input().split())

rockList = list(map(int, input().split()))

visited = [False] * num

visited[0] = True

for i in range(num):
    if not visited[i]:
        continue
    for j in range(i + 1, num):
        cost = (j - i) * (1 + abs(rockList[j] - rockList[i]))
        if cost <= power:
            visited[j] = True
if visited[-1] == True:
    print("YES")
else:
    print("NO")