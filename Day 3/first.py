import csv
import math

def map_getter():
    raw_csv = open("map.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_output = [row[0] for row in csv_list]
    csv_output.pop(0)

    return csv_output

def mapper(guide, row_iter, position_iter):
    position = 0
    row_count = 0
    tree_count = 0
    width = len(guide[0])
    for row in guide:
        if row_count % row_iter == 0:
            if position >= width:
                position = position - width

            if row[position:position + 1] == '#':
                tree_count += 1

            position += position_iter
            
        row_count += 1

    return tree_count

orders = [(1,1), (1,3), (1,5), (1,7), (2,1)]

sled = map_getter()
sums = [mapper(sled, path[0], path[1]) for path in orders]
result = math.prod(sums)


print(sums)
print(result)