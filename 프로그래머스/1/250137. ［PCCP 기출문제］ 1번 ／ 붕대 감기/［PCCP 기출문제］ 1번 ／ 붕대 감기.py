def solution(bandage, health, attacks):
    answer = 0
    now_health = health
    cnt = 0
    pointer = 0
    for i in range(0, attacks[-1][0] + 1):
        if i == attacks[pointer][0]:
            now_health -= attacks[pointer][1]
            pointer += 1
            cnt = 0
            if now_health < 0:
                return -1
        elif now_health == health:
            continue
        else:
            now_health += bandage[1]
            cnt += 1
            if cnt == bandage[0]:
                now_health += bandage[2]
                cnt = 0
            if now_health > health:
                now_health = health                
        print(i, now_health)
    return now_health if now_health > 0 else -1