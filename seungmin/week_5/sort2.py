# 일단 길이가 1인 애들을 정렬시킨다
# 그다음에 길이가 2인 애들을 정렬시키고 인서트

# def solution(numbers):
#     for numbers


numbers = [3, 30, 34, 35, 31, 37,  5, 9]
size = 4
new_numbers = []

for i in numbers:
    num_str = str(i)
    len_diff = size - len(num_str)
    if len_diff == 0:
        new_numbers.append(num_str)
    elif len_diff == 3:
        new_numbers.append("111" + num_str)
    elif len_diff == 2:
        if num_str[0] < num_str[1]:
            new_numbers.append("99" + num_str)
        else:
            new_numbers.append("00" + num_str)
    elif len_diff == 1:
        if num_str[0] < num_str[1]:
            new_numbers.append("9" + num_str)
        else:
            new_numbers.append("00" + num_str)

print(numbers)
print(new_numbers)

