from random import shuffle

# this list with magic square
# square is magic if the sum of each rows, columns and diagonals is 15
magic_square1 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]


def create_numbers_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle(numbers)
    magic_square = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            magic_square[i][j] = numbers[j]
        numbers = numbers[3:]
    return magic_square


def pictured_square(list_of_numbers):
    for i in range(3):
        print('_' * 13)
        for j in range(3):
            print(f'| {list_of_numbers[i][j]} ', end='')
        print('|')
    print('_' * 13)


def total_rows_columns(list_of_numbers):
    magic_rows_columns = True
    for i in range(3):
        total_rows = 0
        total_columns = 0
        for j in range(3):
            total_rows += list_of_numbers[i][j]
            total_columns += list_of_numbers[j][i]
        if total_columns == 15 and total_rows == 15:
            continue
        else:
            magic_rows_columns = False
            break
    return magic_rows_columns


def total_diagonals(list_of_numbers):
    total_diagonal1 = 0
    total_diagonal2 = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                total_diagonal1 += list_of_numbers[i][i]
            if i + j == len(list_of_numbers) - 1:
                total_diagonal2 += list_of_numbers[i][j]
    if total_diagonal1 == 15 and total_diagonal2 == 15:
        print('\nThis square is magic!')


def main():
    list_of_numbers = create_numbers_list()
    pictured_square(list_of_numbers)
    is_rows_columns_15 = total_rows_columns(list_of_numbers)
    if is_rows_columns_15:
        total_diagonals(list_of_numbers)
    else:
        print('\nSquare is not magic!')


main()
