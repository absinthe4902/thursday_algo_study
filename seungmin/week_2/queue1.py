from collections import deque

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]


def solution(bridge_length, weight, truck_weights):
    answer = 0
    brid = [0] * bridge_length
    weight_qu = list(reversed(truck_weights))
    total_we = 0

    while brid:
        answer = answer + 1
        t = brid.pop(0)
        total_we -= t

        if truck_weights:
            if total_we + truck_weights[0] <= weight:
                tt = truck_weights.pop(0)
                brid.append(tt)
                total_we += tt
            else:
                brid.append(0)

    return answer

print(solution(bridge_length, weight, truck_weights))