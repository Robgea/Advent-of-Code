import csv

def pass_getter():
    raw_csv = open("passes.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [entry[0] for entry in csv_list]
    
    return return_list


def reader(passes):
    output_list = []
    for board_pass in passes:
        row_nums = [x for x in range(128)]
        seat_nums = [y for y in range(8)]
        row = board_pass[:7]
        seat = board_pass[7:]

        row_res = ticket_reader(row, row_nums)
        seat_res = ticket_reader(seat, seat_nums)
        
        id_num = (row_res * 8) + seat_res
        
        output_list.append(id_num)

    return output_list


        

def ticket_reader(tick, nums):
    num_len = len(nums)
    num_div = int(num_len/2)

    if (tick[0] == 'F') or (tick[0] == 'L'):
        return_nums = nums[:num_div]

    elif (tick[0] == 'B') or (tick[0] == 'R'):
        return_nums = nums[num_div:]

    if len(return_nums) == 1:
        return return_nums[0]

    else:
        return ticket_reader(tick[1:], return_nums)

def id_finder(id_list):
    id_list.sort()
    
    candidates = []
    candidate_num = 67
    for x in id_list:
        if x == candidate_num + 1:
            pass
        else: 
            candidates.append(x - 1)

        candidate_num = x

    print(candidates)
    





boarders = pass_getter()
large_id = reader(boarders)
id_finder(large_id)