# test
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

# first try
# dict의 getOrDefault 를 쓰는 것 보다 예외로 처리해주는게 더 빨랐다.
def solution1(participant, completion):
    interval = dict.fromkeys(completion, 1)

    for player in participant:
        try:
            interval[player] += 1
        except:
            return player

    for key in interval:
        if interval[key] % 2 != 0:
            return key

    return None

# participant 가 모두 유저가 들어가 있어서 거기에 먼저 다 넣고 completion 을 구했어야 했다.
def solution(participant, completion):
    interval = {}

    for player in participant:
        try:
            interval[player] += 1
        except:
            interval[player] = 1

    for finished in completion:
        interval[finished] -= 1

    for target_player in interval:
        if interval[target_player] != 0:
            return target_player

    return None
