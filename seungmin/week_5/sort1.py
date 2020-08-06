def solution(array, commands):
    answer = []

    for i in commands:
        start = i[0]
        end = i[1]
        target = i[2]

        sub_arr = array[start - 1:end]
        answer.append(sorted(sub_arr)[target - 1])
    return answer


# 배열에 있는 값을 한 줄로 변수만 나열하면 빼주는 아주 재미있는 방법
# 배열의 길이랑 변수의 길이를 맞게 해야 오류가 안 난다.
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer



array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))