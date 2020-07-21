# 못 풀었다.
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    bridge = deque([truck.popleft()])
    length = bridge_length
    last_length = length

    while bridge:
        answer += 1
        length -= 1
        last_length -= 1
        if sum(bridge) <= weight:
            if truck:
                bridge.append(truck.popleft())
                temp_length = bridge_length - length
                length += temp_length
                last_length = temp_length

        if last_length == -1:
            if bridge:
                bridge.popleft()

    return answer