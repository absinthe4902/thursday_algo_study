
# 너무 어려워서 못 풀겠다..

def solution(clothes):
    answer = ''
    wear = {}
    for closet in clothes:
        try:
            wear[closet[1]].append(closet[0])
        except:
            wear[closet[1]] = [closet[0]]

    print(wear)
    return answer