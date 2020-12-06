with open("Advent_6_DeclarationForms.txt", "r") as text_file:
    text = text_file.read()
    text_list = text.split("\n\n")

    compiled_text_each_line = []
    for entry in text_list:
        compiled_text_each_line.append(entry.split("\n"))
    del(compiled_text_each_line[-1][-1])    # newline which my text program automatically adds at the end

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


# TODO
total_number_2 = 0
for entry in compiled_text_each_line:
    for line in entry:
        if line == entry[0]:
            list_of_matching_characters = list(line)
        else:
            for character in list_of_matching_characters:
                if character not in line:
                    list_of_matching_characters.remove(character)

    num_of_matching_letters = len(list_of_matching_characters)
    total_number_2 += num_of_matching_letters

print(f"Solution to the second Question: {total_number_2}")  # 3810 too high

# another solution: search for the shortest entry and check against other entries

total_num_3 = 0
for entry in compiled_text_each_line:
    line_length = 26
    for line in entry:
        if len(line) < line_length:
            line_length = len(line)
            shortest_line = list(line)

    for line in entry:
        for character in shortest_line:
            if character not in line:
                shortest_line.remove(character)
    line_length = len(shortest_line)
    total_num_3 += line_length

print(total_num_3)  # 3737 too high
