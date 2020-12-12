import copy

with open("Advent_7_Bags.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_lines = []
    for line in text_lines:
        compiled_lines.append(line.replace(".\n", ""))

import re

bag_regex = re.compile(r"""
                        (\d??)
                        \s?
                        (\w*?\s\w*?)
                        \sbag
                        """, re.VERBOSE)

dict_of_all_bags = {}
for line in compiled_lines:
    res = re.findall(bag_regex, line)
    dict_of_all_bags[res[0][1]] = []
    for items in res:
        if items == res[0]:
            continue
        else:
            # dict_of_all_bags[res[0][1]].append(items[0])          # adds number of each contained bag
            dict_of_all_bags[res[0][1]].append(items[1])


def bottom_up_search(bag_type, bag_dict, list_of_all_bags=[]):
    list_of_all_bags.append(bag_type)
    for key in bag_dict.keys():
        if bag_type in bag_dict[key]:

            bottom_up_search(key, bag_dict, list_of_all_bags)
        else:
            continue

    removed_duplicates = []
    [removed_duplicates.append(x) for x in list_of_all_bags if x not in removed_duplicates]
    return removed_duplicates


part_1 = len(bottom_up_search("shiny gold", dict_of_all_bags))-1
print(part_1)


dict_of_all_bags_with_numbers = {}
for line in compiled_lines:
    res = re.findall(bag_regex, line)
    dict_of_all_bags_with_numbers[res[0][1]] = []
    for items in res:
        if items == res[0]:
            continue
        else:
            if items[0] == "":
                amount = 0
            else:
                amount = int(items[0])
            dict_of_all_bags_with_numbers[res[0][1]].append([amount, items[1]])

print(dict_of_all_bags_with_numbers)


def contained_bags(bag_type, bag_amount, bag_dict):
    content = copy.deepcopy(bag_dict[bag_type])     # mistake I made: dicts are mutable
    for i in range(len(content)):
        content[i][0] *= bag_amount

    return content


def search_through_bag(bag_type, bag_amount, bag_dict):
    all_contained_bags = []
    bags_to_search_through = [[bag_amount, bag_type]]

    while len(bags_to_search_through) > 0:
        for bag in bags_to_search_through:
            if bag[0] != 0:
                all_contained_bags.append(bag)
                contents = contained_bags(bag[1], bag[0], bag_dict)
                for bags in contents:
                    bags_to_search_through.append(bags)
            bags_to_search_through.remove(bag)

    return all_contained_bags


golden_content = search_through_bag("shiny gold", 1, dict_of_all_bags_with_numbers)
number_of_bags = 0
for item in golden_content:
    number_of_bags += item[0]

print(number_of_bags-1)
