import csv
from collections import Counter

def form_getter():
    raw_csv = open("forms.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    csv_list.append([])
    
    return csv_list

def form_reader(forms):
    count = 0
    group_count = 0
    let_count = Counter()
    for entry in forms:
        if len(entry) == 0:
            for let in let_count:
                if let_count[let] == group_count:
                    count += 1
            let_count = Counter()
            group_count = 0

        else:
            for char in entry[0]:
                let_count[char] += 1
            group_count += 1

    return count

answers = form_getter()
count = form_reader(answers)

print(count)

