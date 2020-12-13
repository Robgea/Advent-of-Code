
check_num = 1001287
bus_nums = "13,x,x,x,x,x,x,37,x,x,x,x,x,461,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,739,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,23"


def time_check(input_string, check_num):
    const_string = input_string.split(',')
    test_dict = {int(num) : int(num) - (check_num % int(num)) for num  in const_string if num != 'x'}

    new_num = 999
    for key in test_dict:
        if new_num > test_dict[key]:
            new_num = test_dict[key]
            result = test_dict[key] * key

    print(result)
    

time_check(bus_nums, check_num)