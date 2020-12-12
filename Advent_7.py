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
            dict_of_all_bags_with_numbers[res[0][1]].append(amount)
            dict_of_all_bags_with_numbers[res[0][1]].append(items[1])

print (dict_of_all_bags_with_numbers)


# contained bags is a list of [[already parsed bags][bags to parse]] with their amount
def top_down_search(bag_type, bag_dict, contained_bags=[[], []]):
    if len(contained_bags[0]) == 0:
        contained_bags[1].append([1, bag_type])

    for bag_and_amount in contained_bags[1]:
        number = bag_and_amount[0]
        bag = bag_and_amount[1]
        inside_content = bag_dict[bag]
        if inside_content[0] != 0:
            for x in range(len(inside_content)):
                if type(inside_content[x]) == int:
                    inside_content[x] *= number
                    contained_bags[1].append([inside_content[x], inside_content[x+1]])
        contained_bags[0].append(bag_and_amount)
        contained_bags[1].remove(bag_and_amount)

    if len(contained_bags[1]) != 0:
        top_down_search(bag_type, bag_dict, contained_bags)
    else:
        return contained_bags


print(top_down_search("shiny gold", dict_of_all_bags_with_numbers))
