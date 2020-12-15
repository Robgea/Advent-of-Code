import sys

sys.setrecursionlimit(2500)

nums_list = [16,1,0,18,12,14,19,]

def number_game(input_list):

    if len(input_list) == 2020:
        return input_list
    
    reversed_list = input_list[::-1]
    new_list = input_list

    if reversed_list[0] in reversed_list[1:]:
        last_index = reversed_list[1:].index(reversed_list[0])
        distance =  last_index + 1
        new_list.append(distance)
        return number_game(new_list)

    if reversed_list[0] not in reversed_list[1:]:
        new_list.append(0)
        return number_game(new_list)

test = number_game(nums_list)
print(test)