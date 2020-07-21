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





## 다른 사람의 풀이인데 너무 잘 풀어서 기록용으로
# def solution(genres, plays):
#     answer = []
#     dic = {}
#     album_list = []
#     for i in range(len(genres)):
#         dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
#         album_list.append(album(genres[i], plays[i], i))
# 
#     dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
#     album_list = sorted(album_list, reverse=True)
#
#
#
#     while len(dic) > 0:
#         play_genre = dic.pop(0)
#         print(play_genre)
#         cnt = 0;
#         for ab in album_list:
#             if play_genre[0] == ab.genre:
#                 answer.append(ab.track)
#                 cnt += 1
#             if cnt == 2:
#                 break
#
#     return answer
#
# class album:
#     def __init__(self, genre, play, track):
#         self.genre = genre
#         self.play = play
#         self.track = track
#
#     def __lt__(self, other):
#         return self.play < other.play
#     def __le__(self, other):
#         return self.play <= other.play
#     def __gt__(self, other):
#         return self.play > other.play
#     def __ge__(self, other):
#         return self.play >= other.play
#     def __eq__(self, other):
#         return self.play == other.play
#     def __ne__(self, other):
#         return self.play != other.play
