# test
# phone_book = ['119', '97674223', '1195524421']

# 해시를 사용하지 않고 풀었다
def solution(phone_book):
    phone_book.sort()
    sliced = []
    first = phone_book[0]

    for num in range(1, len(phone_book)):
        sliced.append(phone_book[num][0:len(first)])

    if first in sliced:
        return False

    return True
