# test
# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 600, 501, 800, 900]


def solution(genres, plays):
    total = {}
    frequency_order = {}
    result = []

    # collect same gen
    for n in range(len(genres)):
        try:
            total[genres[n]].update({n: plays[n]})
            frequency_order[genres[n]] += plays[n]
        except:
            total[genres[n]] = {n: plays[n]}
            frequency_order[genres[n]] = plays[n]

    # sort gen by play frequency
    for music in total.keys():
        total[music] = sorted(total[music].items(), key=lambda item: item[1], reverse=True)

    list_play_order = sorted(frequency_order.items(), key=lambda item: item[1], reverse=True)

    for play_order in list_play_order:
        if len(total[play_order[0]]) < 2:
            result.append(total[play_order[0]][0][0])
        else:
            result.append(total[play_order[0]][0][0])
            result.append(total[play_order[0]][1][0])

    return result
