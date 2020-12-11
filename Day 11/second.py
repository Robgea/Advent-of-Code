import csv
from collections import Counter

def form_getter():
    raw_csv = open("seat_map.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [f'.{row[0]}.' for row in csv_list]
    
    return return_list

def row_reader(input_list):

    seat_stable = False
    result_count = Counter()
    run_count = 0

    while seat_stable == False:

        run_count += 1

        print(f'New run through. run_count == {run_count}')
        change_count = 0
        seated = 0
        new_map = []

        row_index = 0

        for row in input_list:
            new_row = ''
            seat_index = 0

            for seat in row:

                if seat == '.':
                    new_row = f'{new_row}.'
                elif seat == 'L':

                    neighbors = neighbor_check(input_list, row_index, seat_index)
                    if neighbors == 0:
                        new_row = f'{new_row}#'
                    else:
                        new_row = f'{new_row}L'


                elif seat == '#':
                    neighbors = neighbor_check(input_list, row_index, seat_index)
                    if neighbors >= 5:
                        new_row = f'{new_row}L'
                    else:
                        new_row = f'{new_row}#'

                else:
                    print(f'Something bad has happened in row {row_index} seat {seat_index}\n {row}')


                seat_index += 1

            if new_row != row:
                change_count += 1

            new_map.append(new_row)


            row_index += 1

        input_list = new_map

        if change_count == 0:
            for row in new_map:
                print(row)
                for char in row:
                    result_count[char] += 1

            print(f'We have a result. {result_count}')
            seat_stable = True


def neighbor_check(seat_map, row_num, seat_num, code_check = False):
    empty_count = 0
    full_count = 0
    left_check = seat_map[row_num][:seat_num]
    right_check = seat_map[row_num][seat_num + 1:]
    left_check = left_check[::-1]

    upper_check = ''
    lower_check = ''
    row_index = 0

    for row in seat_map:
        if row_num > row_index:
            upper_check = f'{row[seat_num]}{upper_check}'
        if row_index > row_num:
            lower_check = lower_check + row[seat_num]

        row_index += 1

    test_rows = [left_check, right_check, upper_check, lower_check]

    dirs = [(1,1), (-1, 1), (1, -1), (-1, -1)]

    for direc in dirs:
        direc_check = dirs_check(seat_map, row_num, seat_num, direc[0], direc[1])
        test_rows.append(direc_check)

    if code_check == True:
        print(test_rows)

    for row in test_rows:
        for char in row:
            if char == 'L':
                empty_count += 1
                break
            elif char == '#':
                full_count += 1
                break

    return full_count


def dirs_check(seat_map, row_num, seat_num, row_dir, seat_dir):
    row_check = row_num
    seat_check = seat_num
    total_rows = len(seat_map) - 1
    row_len = len(seat_map[2]) - 1

    while (row_check > 0 and total_rows > row_check) and (seat_check > 0 and row_len > seat_check):

        test_char = seat_map[row_check + row_dir][seat_check + seat_dir]
        if test_char != '.':

            return test_char

        row_check += row_dir
        seat_check += seat_dir

    return '.'


check = form_getter()
row_reader(check)
