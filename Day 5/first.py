import csv

def pass_getter():
    raw_csv = open("passes.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [entry[0] for entry in csv_list]
    
    return return_list


def reader(passes):
    output_num = 0
    for board_pass in passes:
        row_nums = [x for x in range(128)]
        seat_nums = [y for y in range(8)]
        row = board_pass[:7]
        seat = board_pass[7:]

        row_res = ticket_reader(row, row_nums)
        print(f'Row num is {row_res}')
        seat_res = ticket_reader(seat, seat_nums)
        print(f'Seat num is {seat_res}')

        id_num = (row_res * 8) + seat_res
        if id_num > output_num:
            output_num = id_num

    return output_num


        

def ticket_reader(tick, nums):
    num_len = len(nums)
    num_div = int(num_len/2)

    if (tick[0] == 'F') or (tick[0] == 'L'):
        print(f'Taking the front')
        return_nums = nums[:num_div]

    elif (tick[0] == 'B') or (tick[0] == 'R'):
        print(f'Taking the back')
        return_nums = nums[num_div:]

    print(f'{return_nums} {tick}')

    if len(return_nums) == 1:
        print(f'Returning: {return_nums[0]}')
        return return_nums[0]

    else:
        return ticket_reader(tick[1:], return_nums)





boarders = pass_getter()
large_id = reader(boarders)
print(large_id)
