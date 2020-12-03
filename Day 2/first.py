import csv

def password_getter():
    raw_csv = open("passwords.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_output = [row[0] for row in csv_list]
    csv_output.pop(0)

    return csv_output

def splitter(input_list):
    adhesion = 0
    for entry in input_list:
        rules = entry.split(' ')
        nums = rules[0].split('-')
        nums = [int(num) for num in nums]
        letter = rules[1][0:1]
        password = rules[2]
        check_num = letter_count(letter, password)
        if (check_num >= nums[0]) and (nums[1] >= check_num):
            adhesion += 1

    return adhesion

def letter_count(letter, word):
    output_num = 0
    for let in word:
        if let == letter:
            output_num += 1

    return output_num


output = password_getter()
total_num = splitter(output)
print(total_num)