# 접근 방식
# progresses 와 speeds 를 둘 다 큐에 넣고 while 을 돌려본다
# 만약 100이 넘었으면 count ++ 해두기
# 하루가 넘어가는 걸 어떻게 구분할까?
# pop 이 처음 큐의 len 만큼 이뤄지면 넘어가기
from collections import deque


def solution(progresses, speeds):
    answer = []
    prog = deque(progresses); spd = deque(speeds)
    count = 0; index = 0; be100 = 0
    day = len(prog)
    first = prog[0] + spd[0];

    while prog:

        sp_pop = spd.popleft()
        now = prog.popleft() + sp_pop
        if now >= 100 and first >= 100 and be100 >= index:
            count = count + 1
            be100 = be100 + 1
        else:
            prog.append(now)
            spd.append(sp_pop)
        index = index + 1

        if day == index:
            if count != 0:
                answer.append(count)
            count = 0; index = 0
            try:
                first = prog[0] + spd[0]
            except:
                pass
            day = len(prog)
    return answer