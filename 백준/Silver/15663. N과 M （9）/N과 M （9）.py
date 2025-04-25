length, cnt = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

def backtrack(path, used):
    if len(path) == cnt:
        answer.append(tuple(path))
        return
    for i in range(len(arr)):
        if used[i]:
            continue
        used[i] = True
        path.append(arr[i])
        backtrack(path, used)
        path.pop()
        used[i] = False

backtrack([], [False]*length)

answer = sorted(set(answer))  # 중복 수열 제거
for element in answer:
    print(" ".join(map(str, element)))
