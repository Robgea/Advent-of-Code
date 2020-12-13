import sys
from sympy.ntheory.modular import solve_congruence



check_num = 1001287
bus_nums = "13,x,x,x,x,x,x,37,x,x,x,x,x,461,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,739,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,23"


def time_check(input_string, check_num):
    const_string = input_string.split(',')
    print(len(const_string))
    dif_num = 0
    test_list = []

    for entry in const_string:
        if entry == 'x':
            dif_num += 1
        else:
            test_list.append((dif_num, int(entry)))
            dif_num += 1

    print(test_list)

    result = solve_congruence(*test_list)

    print(result[1] - result[0])
    return result

    

result = time_check(bus_nums, check_num)
print(result)