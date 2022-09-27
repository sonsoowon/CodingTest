"""
12-12. 기둥과 보 설치 (1시간 30분)
https://school.programmers.co.kr/learn/courses/30/lessons/60061


<초기 접근 방식>
1-1) 기둥 설치인 경우
올릴 수 있는 기둥이 있는가? => (x, y - 1, 기둥) 확인
올릴 수 있는 보가 있는가? => (x - 1, y, 보) or (x, y, 보) 확인

1-2) 보 설치인 경우
올릴 수 있는 기둥이 있는가? => (x, y - 1, 기둥) or (x + 1, y - 1, 기둥) 확인

2-1) 기둥 삭제인 경우
제거해야 하는 보가 있는가? => (x, y + 1, 보) , (x -1, y + 1, 보) 없으면 가능
제거해야 하는 기둥이 있는가? => (x, y + 1, 기둥) 없으면 가능

2-2) 보 삭제인 경우
제거해야 하는 기둥이 있는가? => 보 삭제할 때 고려해야 하는 조건이 너무 복잡하다 !!


>> 각 설치물의 존재 가능 여부를 기둥/보를 삭제한 리스트 각 요소에 적용해서 판단하자
build_frame의 행이 최대 1000개이니 시간적으로 가능하지 않을까?

<바꾼 접근 방식>
기둥 (x,y)가 존재하려면:
- default 벽면 안으로) 0 <= x <= n, 0 <= y < n
- 바닥 위) y == 0
- 보 한쪽 위) 보(x, y) or 보(x -1, y)
- 기둥 위) 기둥 (x, y-1)

보 (x, y)가 존재하려면:
- default 벽면 안으로) 0 <= x < n, 0 < y <= n
- 한쪽 끝이 기둥 위) 기둥(x, y - 1) or 기둥(x + 1, y-1)
- 보 양쪽 끝이 다른 보와 동시 연결) 보(x - 1, y) and 보(x + 1, y) 


시간복잡도
N개의 행으로 구성된 build_frame에 대하여, 최악의 경우 N/2개의 설치물을 built에 모두 더하고
built에서 단 하나의 설치물도 제거할 수 없는 N/2개의 삭제 명령을 수행해야한다.
O(N^2)

"""

def pillar_exist(built, pos, n):
    x, y = pos
    
    case0 = 0 <= x <= n and 0 <= y < n # default 벽면 안으로 존재
    case1 = y == 0 # 바닥 위에 존재
    case2 = [x, y, 1] in built or [x - 1, y, 1] in built # 보 한쪽 위에 존재
    case3 = [x, y - 1, 0] in built # 기둥 위에 존재

    return case0 and (case1 or case2 or case3)


def paper_exist(built, pos, n):
    x, y = pos
    
    case0 = 0 <= x < n and 0 < y <= n # default 벽면 안으로 존재
    case1 = [x, y - 1, 0] in built or [x + 1, y - 1, 0] in built # 보 한쪽이 기둥 위에 존재
    case2 = [x - 1, y, 1] in built and [x + 1, y, 1] in built # 보 양쪽이 다른 보와 동시에 연결하여 존재

    return case0 and (case1 or case2)
    

def solution(n, build_frame):
    built = []
    for item in build_frame:
        pos = (item[0], item[1])
        
        if item[3]: # 설치
            exist = paper_exist(built, pos, n) if item[2] else pillar_exist(built, pos, n) # 설치 가능 여부 확인
            if exist:
                built.append(item[:3])
        else: # 해당 설치물을 삭제한 후 모든 설치물이 조건에 맞춰 존재할 수 있는 지 확인
            built.remove(item[:3])
            exist = True
            for i in built:
                exist = paper_exist(built, (i[0], i[1]), n) if i[2] else pillar_exist(built, (i[0], i[1]), n)
                if not exist:
                    break
            
            if not exist: # 삭제 후 조건에 부합하지 않는 설치물이 있을 경우 삭제 취소
                built.append(item[:3])
                
    
    return sorted(built, key=lambda item: (item[0], item[1], item[2]))