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

def program(instructions, line_num, acc_num, record_set = None):
    if record_set == None:
        print(f'First call!')
        record_set = {0,}

    print(f'Called again. Line: {line_num}, Acc: {acc_num}')

    instruction = instructions[line_num]
    if instruction[0] == 'nop':
        line_num += 1
        if line_num in record_set:
            return f'Infinite loop begun. Line: {line_num}, Acc: {acc_num}'
        else:
            record_set.add(line_num)
            return program(instructions, line_num, acc_num, record_set = record_set)

    elif instruction[0] == 'acc':
        acc_num += instruction[1]
        line_num += 1
        if line_num in record_set:
            return f'Infinite loop begun. Line: {line_num}, Acc: {acc_num}'
        else:
            record_set.add(line_num)
            return program(instructions, line_num, acc_num, record_set = record_set)

    elif instruction[0] == 'jmp':
        line_num += instruction[1]
        if line_num in record_set:
            return f'Infinite loop begun. Line: {line_num}, Acc: {acc_num}'
        else:
            record_set.add(line_num)
            return program(instructions, line_num, acc_num, record_set = record_set)







raw_intrs = instrs_getter()
instructions = enumerator(raw_intrs)
result = program(instructions, 0, 0)
print(result)
