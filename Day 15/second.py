import sys
from collections import defaultdict
import datetime

sys.setrecursionlimit(30000)


nums_list = [16,1,0,18,12,14,19,]

def number_game(input_list):
    sys.stdout.write(f'Initiated. Time is now: {datetime.datetime.now()}\n')
    sys.stdout.flush()


    runcount = 1

    run_dict = defaultdict(int)

    for num in input_list:
        run_dict[num] = runcount
        runcount += 1
        
    start_num = 0

    while 30_000_001 > runcount:


        if start_num in run_dict:
            new_num = runcount - run_dict[start_num]
            run_dict[start_num] = runcount
            start_num = new_num

        else:
            run_dict[start_num] = runcount
            start_num = 0
        runcount += 1

        if runcount % 10_000 == 0:
            sys.stdout.write(f'Run count is now: {runcount}\n Time is now {datetime.datetime.now()}\n')
            sys.stdout.flush()

    print(run_dict)

    print(start_num)


test = number_game(nums_list)

