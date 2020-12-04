import csv
import re

def passport_getter():
    raw_csv = open("passports.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    print(csv_list)
    
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
            for block in blocks:
                fields = block.split(':')
                check_dict.update({fields[0] : fields[1]})

    return valid_count




def checker(dict_in):
    verification = False
    eye_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if (len(dict_in) == 8) or (len(dict_in) == 7 and 'cid' not in dict_in):
        if num_check(dict_in['byr'], 1920, 2002) == False:
            return False

        if num_check(dict_in['iyr'], 2010, 2020) == False:
            return False

        if num_check(dict_in['eyr'], 2020, 2030) == False:
            return False

        if height_check(dict_in['hgt']) == False:
            return False
        if dict_in['ecl'] not in eye_list:
            return False

        if col_check(dict_in['hcl']) == False:
            return False

        try:
            if len(dict_in['pid']) == 9:
                pid_int = int(dict_in['pid'])
                return True
            else: 
                return False
        except Exception as err:
            print(f'Failed Password ID check. \n Error: {err}\n Rejecting passport.')
            return False

        verification = True

    return verification

def num_check(field, lower, upper):
    try:
        field_num = int(field)
        if (field_num >= lower) and (upper >= field_num):
            return True

        else:
            return False
    except Exception as err:
        print(f'Invalid input data. \n Error: {err}\n Rejecting passport.')
        return False

def height_check(field):
    if field.endswith('in'):
        try:
            field_int = int(field[0:2])
            if (field_int > 58) and (79 > field_int):
                return True
            else:
                return False
        except Exception as err:
            print(f'Invalid height data. \n Error: {err} \n Rejecting passport. ')
            return False
    elif field.endswith('cm'):
        try:
            field_int = int(field[0:3])
            if (field_int > 149) and (194 > field_int):
                return True
            else:
                return False
        except Exception as err:
            print(f'Invalid height data. \n Error: {err} \n Rejecting passport.')
            return False
    
    else:
        return False        

def col_check(colour):
    reg_pat = r'[^#a-f0-9.]'
    if re.search(reg_pat, colour) == True:
        return False
    else:
        return True



passports = passport_getter()
final_count = splitter(passports)
print(final_count)

