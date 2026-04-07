def solution(s):
    answer = []

    for x in s:
        stack = []
        count_110 = 0

        for ch in x:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3] == '1' and stack[-2] == '1' and stack[-1] == '0':
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1

        remain = ''.join(stack)
        idx = remain.rfind('0')

        insert_str = '110' * count_110

        if idx == -1:
            result = insert_str + remain
        else:
            result = remain[:idx + 1] + insert_str + remain[idx + 1:]

        answer.append(result)

    return answer