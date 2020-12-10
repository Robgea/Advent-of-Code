import csv
from collections import Counter


def numbs_getter():
    raw_csv = open("nums.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [int(row[0]) for row in csv_list]
    raw_csv.close()
   
    return return_list

def list_sorter(input_list):
    input_list.sort()

    one_count = 0
    three_count = 0

    test_num = 0

    print(input_list)

    one_step = 0
    num_count = Counter()

    prod_num = 1


    

    for x in input_list:
        if test_num > 0:
            print(f'{x} {old_num}')
            if x - old_num == 1:
                one_count += 1
                one_step += 1

            if x - old_num == 3:
                three_count += 1
                print(f'We had {one_step}s. Great!')
                num_count[one_step] += 1
                if one_step == 4:
                    prod_num *= 7
                if one_step == 3:
                    prod_num *= 4
                
                if one_step == 2:
                    prod_num *= 2
                one_step = 0

            if x - old_num > 3:
                print(f'We have a problem. {x} {old_num}')
        test_num += 1

        old_num = x
    print(prod_num)

    print(f'1 Count: {one_count}, 3 Count: {three_count} \n {one_count * three_count} \n {num_count}')

nums_list = numbs_getter()
list_sorter(nums_list)


print((7 ** 12) * (4 ** 2) * (2 ** 5) * 7)