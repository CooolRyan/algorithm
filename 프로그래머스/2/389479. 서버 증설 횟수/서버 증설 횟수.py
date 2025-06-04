import math

def solution(players, m, k):
    answer = 0
    server = [0] * 24
    for idx, i in enumerate(players):
        threshold = (server[idx] * m) 
        if i > threshold:
            toadd=((i-threshold)//m)
            for j in range(0,k):
                if idx + j > 23:
                    break
                server[idx + j] += toadd
            answer += toadd
            print(toadd, idx)
            
    return answer