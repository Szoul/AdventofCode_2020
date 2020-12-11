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
            dict_of_all_bags_with_numbers[res[0][1]].append(items[0])
            dict_of_all_bags_with_numbers[res[0][1]].append(items[1])

print (dict_of_all_bags_with_numbers)


def top_down_search(bag_type, bag_dict):
    list_of_contained_bags = []

    for key in bag_dict.keys():
        if bag_type == key:
            list_of_contained_bags.append(bag_dict[key])