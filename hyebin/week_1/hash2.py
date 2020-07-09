def solution(phone_book):
    m = min(phone_book)
    phone_book.remove(m)

    for i in phone_book:
        if m == i[:len(m)]:
            return False

    return True

