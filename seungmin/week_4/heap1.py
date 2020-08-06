import heapq


def solution(scoville, K):
    answer = 0
    hp_sco = scoville[:]
    heapq.heapify(hp_sco)

    while hp_sco[0] < K:
        try:
            hp_first = heapq.heappop(hp_sco)
            hp_second = heapq.heappop(hp_sco) * 2
        except IndexError:
            return -1

        heapq.heappush(hp_sco, (hp_first + hp_second))
        answer = answer + 1

    if hp_sco[0] < K:
        return -1

    return answer


scoville = [0,0,0,0]
K = 3

print(solution(scoville, K))