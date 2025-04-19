from collections import defaultdict
num = int(input())

for _ in range(num):
    strin = input()
    cnt = int(input())
    dic = defaultdict(list)
    for i in range(len(strin)):
       dic[strin[i]].append(i)
        
    min_len = float('inf')
    max_len = 0

    for char, val in dic.items():
        if len(val) < cnt:
            continue  

        for i in range(len(val) - cnt + 1):
            start = val[i]
            end = val[i + cnt - 1]
            length = end - start + 1

            min_len = min(min_len, length)

            if strin[start] == strin[end]: 
                max_len = max(max_len, length)

    if min_len == float('inf') or max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)