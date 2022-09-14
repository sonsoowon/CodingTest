"""
11-6. 무지의 먹방 라이브
1 1 7 9 1 3 / 10 -> 3

1 1 1 3 7 9
idx 0 1 4 5 2 3

1 1 1 / 4

0 0 0 / 1


curr=0 next=3
>= 인 이유 : 다 먹어치운 접시가 생겨나는 타이밍. 0~6초 동안 음식을 섭취하고 다 먹어치운 접시가 생긴다.
6초에서 장애 발생 후 다시 먹어야할 때는 새로 생긴 빈접시를 건너뛰어야 하므로 k == 6 인 경우도 포함한다.

k >= 6 * 1
-> k = 4
curr=3 next=4 min=2
k < 2*3

idx[curr:].sort() -> 2 3 5
idx[k%3]

idx 2 3 5

"""



def solution(food_times, k):
    answer = 0
    
    food_len = len(food_times)
    sorted_times = sorted(food_times)
    sorted_idx = sorted(range(food_len), key=lambda x: food_times[x])
    
    curr = 0
    remain_idx = sorted_idx[curr:]
    m = sorted_times[curr]
    
    while k >= m * (food_len - curr) :
        k -= m * (food_len - curr)
        
        # 다음 min time 위치 탐색
        next = curr
        for i in range(food_len - curr):
            if sorted_times[curr + i] > sorted_times[curr]:
                break
            next += 1
        
        if next == food_len:
            break
            
        m = sorted_times[next] - sorted_times[curr]
        curr = next
    
    return answer