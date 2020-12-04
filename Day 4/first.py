import csv

def passport_getter():
    raw_csv = open("passports.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    csv_list.append([])
    
    return csv_list

def splitter(lines):
    check_dict = {}
    valid_count = 0
    for line in lines:
        if len(line) == 0:
            if checker(check_dict) == True:
                valid_count += 1
            check_dict = {}
        else:
            blocks = line[0].split(' ')
            print(blocks)
            for block in blocks:
                fields = block.split(':')
                check_dict.update({fields[0] : fields[1]})

    return valid_count




def checker(dict_in):
    verification = False
    if (len(dict_in) == 8) or (len(dict_in) == 7 and 'cid' not in dict_in):
        verification = True

    return verification

passports = passport_getter()
final_count = splitter(passports)
print(final_count)

