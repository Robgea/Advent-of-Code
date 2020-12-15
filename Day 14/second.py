import csv

def inst_getter():
    with open("instructions.csv", encoding='utf-8') as raw_csv:
        csv_read = csv.reader(raw_csv)
        csv_list = list(csv_read)
        csv_list.pop(0)
        return_list = [row[0].split(' = ') for row in csv_list]
        
    return return_list

def inst_reader(instrs):

    output_dict = {}
    mask = ''
    output_sum = 0


    for line in instrs:
        if line[0].startswith('mask'):
            x_count = 0
            mask = line[1]

            for char in mask:
                if char == 'X':
                    x_count += 1


        elif line[0].startswith('mem'):
            input_num = int(line[1])
            input_mem = str(bin(int(line[0][4:-1])))[2:].zfill(36)
            output_mems = ['',]
            index_num = 0


            for char in input_mem:
                if mask[index_num] == 'X':
                    output_mems = list_adder(output_mems, 'X')
                elif mask[index_num] == '1':
                    output_mems = list_adder(output_mems, '1')
                elif mask[index_num] == '0':
                    output_mems = list_adder(output_mems, char)

                index_num += 1

            for address in output_mems:
                output_dict.update({int(address, base = 2) : input_num})

    

    for key in output_dict:
        output_sum += output_dict[key]

    print(output_sum)


def list_adder(input_list, char):
    output_list = []
    if char == 'X':
        for string in input_list:
            output_list.append(f'{string}1')
            output_list.append(f'{string}0')
    if char == '1':
        output_list = [f'{entry}1' for entry in input_list]

    if char == '0':
        output_list = [f'{entry}0' for entry in input_list]

    return output_list 


instructions = inst_getter()
inst_reader(instructions)
