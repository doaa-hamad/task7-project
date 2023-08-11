# ----------- Q1 -----------
def drow_pattern(num_rows):
    i = 1
    while i != num_rows + 2:
        for num in range(1, i):
            print(str(num), end=' ')
        i += 1
        print('')


drow_pattern(5)


# ----------- Q2 -----------
# ==== way1 : According Question
def calculate_sum(num_rows):
    sum_nums = 0
    for num in range(num_rows + 1):
        sum_nums += num
    return sum_nums


print(calculate_sum(10))


# ----------- Q3 -----------
def drow(name):
    i = 0
    while i != len(name) + 1:
        for num in range(i):
            print(name[num], end='')
        i += 1
        print('')

    i = len(name) - 1
    while i != 0:
        for num in range(i):
            print(name[num], end='')
        i -= 1
        print('')


drow('zakaria')


# ----------- Q4 -----------
def reverse_word(name):
    char = len(name) - 1
    while char != -1:
        print(name[char], end='')
        char -= 1


reverse_word('Zakaria')


# ----------- Q5 -----------
def print_number_descending_order(num):
    while num != 0:
        print(num, end=' ')
        num -= 1


print_number_descending_order(10)


# ----------- Q6 -----------
def Q6():
    for num in range(0, 55, 5):
        if num == 0:
            continue
        print(num, end=' ')


Q6()


