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

    for line in instrs:
        if line[0].startswith('mask'):
            mask = line[1]
            print(f'New mask found: {mask}')
        elif line[0].startswith('mem'):
            input_num = str(bin(int(line[1])))[2:].zfill(36)
            index_num = 0
            output_num = ''

            for char in input_num:
                if mask[index_num] != 'X':
                    output_num = f'{output_num}{mask[index_num]}'
                else:
                    output_num = f'{output_num}{char}'

                index_num += 1

            output_dict.update({line[0][4:-1] : output_num})

    output_sum = 0

    for key in output_dict:
        output_sum += int(output_dict[key], base = 2)

    print(output_sum)



instructions = inst_getter()
inst_reader(instructions)
