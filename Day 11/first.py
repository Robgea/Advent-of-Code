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
                    if '#' not in neighbors:
                        new_row = f'{new_row}#'
                    else:
                        new_row = f'{new_row}L'

                elif seat == '#':
                    neighbors = neighbor_check(input_list, row_index, seat_index)
                    count_check = Counter(neighbors)
                    if count_check['#'] > 3:
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
                for char in row:
                    result_count[char] += 1

            print(f'We have a result. {result_count}')
            seat_stable = True


def neighbor_check(seat_map, row, seat):
    neighbor_string = f'{seat_map[row - 1][seat - 1: seat + 2]}{seat_map[row][seat -1:seat + 2: 2]}{seat_map[row + 1][seat - 1: seat + 2]}'
    return neighbor_string


check = form_getter()
row_reader(check)

