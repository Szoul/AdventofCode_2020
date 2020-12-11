with open("Advent_6_DeclarationForms.txt", "r") as text_file:
    text = text_file.read()
    text_list = text.split("\n\n")

    # for some reason my text-program added a newline at the end
    for entry in range(len(text_list)):
        if text_list[entry].endswith("\n"):
            text_list[entry] = text_list[entry][:-1]

    compiled_text_each_line = []
    for entry in text_list:
        lines = entry.split("\n")
        entry = []
        for line in lines:
            set_line = set(line)
            entry.append (set_line)
        compiled_text_each_line.append(entry)

    compiled_text_whole_entry = []
    for entry in text_list:
        compiled_text_whole_entry.append(entry.replace("\n", ""))

import string
import copy
alphabet_list = list(string.ascii_lowercase)

total_number = 0
for entry in compiled_text_whole_entry:
    non_existing_characters = copy.deepcopy(alphabet_list)
    for character in entry:
        if character in non_existing_characters:
            non_existing_characters.remove(character)

    num_of_different_letters = 26-len(non_existing_characters)
    total_number += num_of_different_letters

print(f"Solution to the first Question: {total_number}")


total_num2 = 0
for entry in compiled_text_each_line:
    intersection = set.intersection(*entry)
    total_num2 += len(intersection)

print(total_num2)
