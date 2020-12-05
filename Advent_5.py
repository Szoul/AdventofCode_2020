with open("Advent_5_Boarding.txt", "r") as text_file:
    text = text_file.readlines()
    text_list = []
    for line in text:
        text_list.append([line.strip()[:7], line.strip()[7:]])


def find_row(binary_code, possible_rows=[0, 128], lower="F", higher="B"):
    middle = possible_rows[1] - (possible_rows[1] - possible_rows[0]) / 2

    if len(binary_code) == 1:
        if binary_code[0] == lower:
            return int(possible_rows[0])
        elif binary_code[0] == higher:
            return int(possible_rows[1]-1)

    if binary_code[0] == lower:
        binary_code = binary_code[1:]
        return find_row(binary_code, [possible_rows[0], middle], lower, higher)
    elif binary_code[0] == higher:
        binary_code = binary_code[1:]
        return find_row(binary_code, [middle, possible_rows[1]], lower, higher)


def calculate_ID(partitioning_list):
    return find_row(partitioning_list[0])*8 + find_row(partitioning_list[1], [0, 8], "L", "R")


highest_id = 0
for id_list in text_list:
    current_id = calculate_ID(id_list)
    if highest_id < current_id:
        highest_id = current_id
print(highest_id)

# my seat is the one tha tis missing in the list
# the first and last row are missing from this flight
# i know im not in one of the missing rows

all_IDs = []
for id_list in text_list:
    current_id = calculate_ID(id_list)
    all_IDs.append(current_id)
all_IDs.sort()

for i in range(len(all_IDs)):
    if all_IDs[i]+1 != all_IDs[i+1]:
        print(all_IDs[i]+1)
        break
