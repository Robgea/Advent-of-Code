import csv
import sys

def numbs_getter():
    raw_csv = open("numbs.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [int(row[0]) for row in csv_list]
    raw_csv.close()
   
    return return_list

def sum_dict_builder(numbs_list):
    run_count = 0
    output_dict = {}

    for num in numbs_list:
        if run_count > 24:
            first_ind = run_count - 25
            check_set = numb_summer(numbs_list[first_ind:run_count])
            output_dict.update({str(num) : check_set})
        else:
            holding_set = set([num + 1, num + 2, num])
            output_dict.update({str(num) : holding_set})

        run_count += 1

    return output_dict


def numb_summer(input_list):
    run_count = 0
    return_set = set()
    for num in input_list:
        if run_count == len(input_list) - 1:
            return return_set
        else:
            add_list = input_list[run_count + 1:]
            for add in add_list:
                return_set.add(num + add)

        run_count += 1


def numb_checker(input_dict):
    for key in input_dict:
        try:
            if int(key) not in input_dict[key]:
                print(f'Found one! {key} {input_dict[key]}')
                return_num = int(key)

        except Exception as err:
            print(f'Ran into a problem. {err}\n {key}, {input_dict[key]}')

    return return_num


def vuln_finder(vuln_target, vuln_dict):
    vuln_list = [int(key) for key in vuln_dict if vuln_target > int(key)]

    index_num = 0

    for num in vuln_list:
        if index_num % 10 == 0:
            sys.stdout.write('Progress is being made!')
            sys.stdout.flush()
        end_num = len(vuln_list) - 1
        for num in vuln_list[index_num:end_num]:
            check_list = vuln_list[index_num:end_num]
            if sum(check_list) == vuln_target:
                print(f'Got it! {check_list}')
                return check_list
            end_num -= 1

        index_num += 1



    print(vuln_list)
    print(len(vuln_list))

init_list = numbs_getter()
check_dict = sum_dict_builder(init_list)
vuln_num = numb_checker(check_dict)
vuln_found = vuln_finder(vuln_num, check_dict)
print(vuln_found)
vuln_found.sort()
print(vuln_found)
print(sum((vuln_found[0], vuln_found[-1])))