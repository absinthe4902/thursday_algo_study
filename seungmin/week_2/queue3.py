import collections


def solution(priorities, location):
    answer = []
    wait = [i for i in range(len(priorities))]
    my_pri = priorities[location]
    zip_wait = collections.deque(zip(priorities, wait))
    sorted_pri = sorted(priorities, reverse=True)
    index = 0
    max = sorted_pri[0]

    while index < len(priorities) - 1:
        if max == zip_wait[0][0]:
            answer.append(zip_wait.popleft())
            index = index + 1
            max = sorted_pri[index]
        else:
            out = zip_wait.popleft()
            zip_wait.append(out)

    answer.append(zip_wait.popleft())

    return answer.index((my_pri, location)) +1


# 결과 4 나와야 한다.
pri = [3, 3, 4, 2]
loc = 3
print(solution(pri, loc))