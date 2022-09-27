"""
12-7. 럭키 스트레이트 (5min)

"""


def solution(score):
    left = score[:len(score)//2]
    right = score[len(score)//2:]

    left_sum = sum(list(map(int, list(left))))
    right_sum = sum(list(map(int, list(right))))

    return 'LUCKY' if left_sum == right_sum else 'READY'

n = int(input())
print(solution(str(n)))
