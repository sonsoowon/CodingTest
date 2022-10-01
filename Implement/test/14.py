"""
12-14. 외벽 점검 (2시간)

초기 풀이: 거의 모든 테스트 케이스에 대해 시간초과가 떴다
알고리즘이 어딘가 잘못되었다

두번째 풀이: 시간초과는 뜨지 않았지만 정확성 64%.. 고려하지 않은 부분이 있나보다



"""

# def solution(n, weak, dist):
#     answer = 0
    
#     if len(weak) == 1:
#         return 1
    
#     while len(weak):
#         if not len(dist):
#             answer = -1
#             break
        
#         w = len(weak)
#         for k in range(1, w):
#             max_dist = 0
#             start, end = 0, 0
#             for s, e in zip(range(w), range(k, w + k)):
#                 temp_dist = weak[e % w] - weak[s] if e % w > s else 12 + weak[e % w] - weak[s]
#                 if max_dist < temp_dist:
#                     max_dist = temp_dist
#                     start, end = s, e % w 
                    
#             # (w - (k - 1)) 개 취약점 점검 가능
#             if n - max_dist <= dist[-1]:
#                 dist.pop()
#                 remain_start = (start + 1) % w
#                 weak = weak[remain_start : end] if remain_start <= end else weak[remain_start:] + weak[:end] # 남은 취약점 배열 업데이트
#                 # 등호 똑바로 쓰자!!
#                 # remain_start < end 로 해서 취약점을 모두 점검한 경우에 weak가 빈 리스트로 업데이트 되지 않아
#                 # weak[remain_start:] + weak[:end] (remain_start == end) 로 weak에 변동 X
#                 weak = sorted(weak)
#                 answer += 1
#                 break
    
#     return answer

def check_weaks(start, end, w):
    if start == end: # 외벽 한바퀴를 다 도는 경우
        return True
    elif start < end: # 정북 방향 지점(0)을 제외하고 도는 경우
        return start <= w and w <= end
    else: # 정북 방향 지점(0)을 포함하고 도는 경우
        return start <= w or w <= end
    
def solution(n, weak, dist):
    answer = 0
    
    if dist[-1] >= n or len(weak) == 1:
        return 1
    
    for d in dist[::-1]: 
        if not len(weak):
            break
            
        min_dist = n
        remain_weak = weak
        for i in range(len(weak)):
            start = weak[i]
            end = (weak[i] + d) % n    
            temp_weak = [w for w in weak if not check_weaks(start, end, w)]
            remain_dist = min(temp_weak[-1] - temp_weak[0], temp_weak[0] - temp_weak[-1] + n) if len(temp_weak) else 0

            if remain_dist < min_dist:
                min_dist = remain_dist
                remain_weak = temp_weak

        weak = remain_weak
        answer += 1
    
    
    return answer if len(weak) == 0 else -1


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))
