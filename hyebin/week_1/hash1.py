def solution(phone_book):
    for i in phone_book:
        c = 0
        for j in phone_book:
            if i in j and i[:1] == j[:1]:
                c += 1
        if c > 1:
            return False

    return True


# 두번째
def solution(phone_book):
    m = min(phone_book)
    phone_book.remove(m)

    for i in phone_book:
        if m == i[:len(m)]:
            return False

    return True
