"""
12-9. 문자열 압축 (다른 풀이 참조)
https://school.programmers.co.kr/learn/courses/30/lessons/60057

문자열 s의 길이가 N일 때,
N + N/2 + N/3 + ... + N/(N/2) = N{1 + 1/2 + 1/3 + ... + 1/(N/2)} => O(NlogN) 아닌가?
왜 O(N^2) 이지?? 더 알아보고 정리하기

"""

def compress(words):
    count = 1
    result = 0

    """
    TIL 1. zip을 활용한 리스트의 전후 요소 비교:
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                count += 1
            else:
                curr = words[i]
                result += ...
                count = 1
        
        리스트의 마지막 두 단어가 다를 경우 words[-1]이 1개 존재함을 result에 포함하지 못하므로
        for문 이후에 추가적인 코드가 필요하다. zip은 이 문제를 아래와 같이 해결한다.
    """
    for curr, next in zip(words, words[1:] + ['']):
        if curr == next:
            count += 1
        else:
            # TIL 2. 불필요한 연산 줄이기: 
            # compress(words) 함수에서 압축한 문자열의 형태가 아닌 "길이"만 바로 계산하게 할 것
            result += len(curr) + len(str(count)) if count > 1 else len(curr)
            count = 1
            
    return result

def solution(s):
    results = []
    """
    TIL 3. 반복문의 range와 입력값의 범위에 주의하자:
        for token_len in range(1, len(s) // 2) 의 문제점
        1)  len(s) // 2 - 1 까지만 부여해서 token_len == len(s) // 2인 경우 포함X
            ababcdcdababcdcd에서 최소 길이 12로 정답 9와 다른 결과 도출
        2)  런타임 에러: s의 길이가 1인 경우 results가 빈 배열이라 min([]) 에서 에러 발생
            len(s)를 token_len으로 포함해서 반복문 실행해야 함
    """
    for token_len in list(range(1, len(s) // 2 + 1)) + [len(s)]:
        results.append(compress([s[i:i+token_len] for i in range(0, len(s), token_len)]))
    
    return min(results)
        
            