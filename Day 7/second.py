import csv


def bags_getter():
    raw_csv = open("bag_list.csv", encoding='utf-8')
    csv_read = csv.reader(raw_csv)
    csv_list = list(csv_read)
    csv_list.pop(0)
    return_list = [row[0][:-1] for row in csv_list]
   
    return return_list

def rule_splitter(bag_list):
    bag_dict = {}

    for rule in bag_list:
        find_num = rule.find('s cont')
        split_num = rule.find('in ')
        contains = []   
        contain_names = rule[split_num + 3:]
        if 'no other bags' in contain_names:
            pass
        else:
            contained_bags = contain_names.split(', ')
            for name in contained_bags:
                num = name[:1]
                bag_name = name[2:]
                if bag_name.endswith('s'):
                    bag_name = bag_name[:-1]
                contains.append((int(num), bag_name))

        bag_dict[rule[:find_num]] = contains

    return bag_dict



def bag_searcher(bag_dict, bag):
    return 1 + sum(num * bag_searcher(bag_dict, sub_bag) for num, sub_bag in bag_dict[bag])






init_bag = 'shiny gold bag'

bags = bags_getter()
test = rule_splitter(bags)
result = bag_searcher(test, init_bag)
print(result)
