import csv

def form_getter():
    raw_csv = open("forms.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    csv_list.append([])
    
    return csv_list

def form_reader(forms):
    count = 0
    let_set = set()
    for entry in forms:
        if len(entry) == 0:
            count += len(let_set)
            let_set = set()
        else:
            new_set = {char for char in entry[0]}
            let_set = let_set|new_set

    return count

answers = form_getter()
count = form_reader(answers)

print(count)

