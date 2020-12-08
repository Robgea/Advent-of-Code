import csv

def bags_getter():
    raw_csv = open("bag_list.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [row[0][:-1] for row in csv_list]
   
    return return_list

def rule_splitter(bag_list, bags):
    search_set = set()

    count = 0

    for bag in bags:

        for rule in bag_list:

            if bag in rule:
                find_num = rule.find('s cont')
                search_set.add(rule[:find_num])



        
    if len(search_set) == len(bags):
        return bags|search_set
    
    else:
        print(f'RECURSION! {len(search_set)} {len(bags)}')
        bags = search_set|bags
        return rule_splitter(bag_list, bags)



first_set = {'shiny gold bag'}

bags = bags_getter()
test = rule_splitter(bags, first_set)
print(test)
print(len(test) - 1)


