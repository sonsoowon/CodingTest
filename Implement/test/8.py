"""
12-8. 문자열 재정렬 (10min)

"""

def solution(string):
    sorted_str = sorted(string)
    nums = []
    for c in sorted_str:
        # 오름차순으로 정렬된 리스트에서 처음 문자가 나타날 때 
        # 모든 숫자를 확인했으므로 반복문을 탈출한다
        if ord(c) > 57:
            break
        nums.append(int(c))

    return ''.join(sorted_str[len(nums):]) + str(sum(nums))

s = input()
print(solution(s))    

