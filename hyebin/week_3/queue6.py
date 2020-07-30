def solution(progresses, speeds):
    answer = []

    while progresses:
        n = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                n += 1
        if n >= 1 :
            answer.append(n)
    return answer
