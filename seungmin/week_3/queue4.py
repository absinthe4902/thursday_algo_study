def solution(arrangement):
    arr = list(arrangement.replace('()', '1', arrangement.count('()')))
    stack = []
    answer = 0
    index = 0
    cutter = 0
    checker = 0
    length = len(arr)
    while index < length:
        temp = arr[index]

        if temp == ')':
            for i in range(index-1, -1, -1):
                if arr[i] == '1':
                    cutter = cutter + 1
                elif arr[i] == '(':
                    arr[i] = '0'
                    answer = answer + cutter + 1
                    cutter = 0
                    break
        index = index + 1
    return answer



cd



print(solution('()(((()())(())()))(())'))

