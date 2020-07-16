def solution(heights):
    answer = [0 for i in range(len(heights))]
    stack = list(heights)

    while len(stack) != 0:
        index = len(stack) - 1
        target = stack.pop()
        for i in range(index - 1, -1, -1):
            if stack[i] > target:
                answer[index] = i + 1
                break

    ## 남이 풀은 코드인데 너무 잘 풀어서 기록용
    #     answer = [0]
    #     stack = list(heights)
    #     max = heights[0]
    #     index = 0

    #     for i in range(1, len(heights)):
    #         if max < heights[i]:
    #             max = heights[i]
    #             index = 0
    #         if heights[i-1] > heights[i]:
    #             index = i
    #         answer.append(index)

    return answer