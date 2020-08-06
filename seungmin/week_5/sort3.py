def solution(citations):
    st_ci = sorted(citations)
    an_arr = []

    for i in range(st_ci[len(st_ci) - 1] // 2 + 1):
        count = 0
        for j in st_ci:
            if j >= i:
                count = count + 1
        if count >= i:
            an_arr.append(i)
    return max(an_arr) if an_arr else 0