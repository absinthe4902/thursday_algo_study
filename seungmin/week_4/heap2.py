import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    candidate = []
    index = 0
    sup_len = len(supplies)

    while stock < k:
        for i in range(index, sup_len, 1):
            if dates[i] <= stock:
                heapq.heappush(candidate, -supplies[i])
                index = index + 1
            else:
                break
        stock += heapq.heappop(candidate) * -1
        answer = answer + 1
    return answer

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30

print(solution(stock, dates, supplies, k))