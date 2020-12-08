import csv


def instrs_getter():
    raw_csv = open("instructions.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [row[0] for row in csv_list]
    raw_csv.close()
   
    return return_list

def enumerator(inst_list):

    enumed = enumerate(inst_list)
    return_dict = {}
    for entry in enumed:
        instrs = entry[1].split(' ')
        return_dict.update({int(entry[0]) : (instrs[0], int(instrs[1]))})

    return return_dict

def program(instructions, line_num, acc_num, swap_set, record_set = None, swap_rule = True):
    if record_set == None:
        print(f'First call! Adding {line_num} to the record set.')
        record_set = {line_num,}

    swap_dict = {'jmp' : 'nop', 'nop' : 'jmp'}


    print(f'Called again. Line: {line_num}, Acc: {acc_num}')

    instruction = instructions[line_num]

    if (instruction[0] in swap_dict) and (swap_rule == True):
        if line_num not in swap_set:
            print(f'Swapping instructions at line: {line_num}.')
            instruction = (swap_dict[instruction[0]], instruction[1])
            swap_set.add(line_num)
            swap_rule = False
        else:
            print(f'Skipping a swap instruction. Line {line_num}\n Swapset: {swap_set}\n')


    if instruction[0] == 'nop':
        line_num += 1
        if line_num > 625:
            print(f'We have found the end-point. Accumulator: {acc_num}.')
            return True

        if line_num in record_set:
            return f'Infinite loop begun. Line: {line_num}, Acc: {acc_num}'

        else:
            record_set.add(line_num)
            return program(instructions, line_num, acc_num, swap_set, record_set = record_set, swap_rule = swap_rule)

    elif instruction[0] == 'acc':
        acc_num += instruction[1]
        line_num += 1
        if line_num > 625:
            print(f'We have found the end-point. Accumulator: {acc_num}')
            return True
        if line_num in record_set:
            return f'Infinite loop begun. Line: {line_num}, Acc: {acc_num}'
        else:
            record_set.add(line_num)
            return program(instructions, line_num, acc_num, swap_set, record_set = record_set, swap_rule = swap_rule)

    elif instruction[0] == 'jmp':
        line_num += instruction[1]

        if line_num > 625:
            print(f'We have found the end-point. Accumulator: {acc_num}')
            return True

        elif line_num in record_set:
            return f'Infinite loop begun. Line: {line_num}, Acc: {acc_num}'
        
        else:
            record_set.add(line_num)
            return program(instructions, line_num, acc_num, swap_set, record_set = record_set,  swap_rule = swap_rule)



swap_set = set()




raw_intrs = instrs_getter()
instructions = enumerator(raw_intrs)

result = False

while result is not True:
    result = program(instructions, 0, 0, swap_set, swap_rule = True)
    print(result)

