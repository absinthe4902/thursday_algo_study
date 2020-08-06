def solution(arrangement):
    answer = 0
    arr = list(arrangement)
    n = 0
    for i in range(len(arr)):
        if arr[i]=='(' and arr[i+1]=='(':
            n += 1
        elif arr[i]=='(' and arr[i+1]==')':
            answer += n
        elif arr[i]==')' and arr[i+1]==')':
            n -= 1
            answer += 1
        
    return answer
