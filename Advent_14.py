import copy

with open("Advent_14_Masks.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = {}
    for line in text_lines:
        if line.startswith("mask"):
            content_key = line.strip().lstrip("mask = ")
            compiled_text[content_key] = []
        else:
            content_value = line.strip().replace("mem[", "").replace("] = ", "|")
            content_value = content_value.split("|")
            content_value[0] = int(content_value[0])
            content_value[1] = int(content_value[1])
            compiled_text[content_key].append(content_value)
# compiled text == { mask:[[value, memory address], ...], ... }


def turn_value_into_36_string_binary(value):
    binary_string = str(bin(value))[2:]
    if len(binary_string) < 36:
        zero_len = 36-len(binary_string)
        binary_string = "0"*zero_len + binary_string

    return binary_string


def apply_mask_and_return_decimal(binary_string, mask):
    result_string = ""
    for i in range(len(binary_string)):
        if mask[i] == "X":
            result_string += binary_string[i]
        else:
            result_string += mask[i]

    decimal = int(result_string, 2)
    return decimal


def update_memory_slots():
    instruction_list = copy.deepcopy(compiled_text)
    updated_memory = {}
    for masks in instruction_list.keys():
        value_list = instruction_list[masks]
        for value_pair in value_list:
            memory_slot = value_pair[0]
            decimal_value = value_pair[1]
            new_decimal_value = apply_mask_and_return_decimal(turn_value_into_36_string_binary(decimal_value), masks)
            updated_memory[memory_slot] = new_decimal_value

    return updated_memory


def calculate_slots(binary_string, mask):
    floating_string = ""
    for i in range(len(binary_string)):
        if mask[i] == "X" or mask[i] == "1":
            floating_string += mask[i]
        elif mask[i] == "0":
            floating_string += binary_string[i]

    paths = [[], []]
    current_path = ""
    for i in floating_string:
        if i.isnumeric():
            current_path += i
        else:
            new_path = current_path + "1"
            current_path += "0"
            if len(new_path) < 36:
                paths[1].append(new_path)
            else:
                paths[0].append(new_path)
    paths[0].append(current_path)

    while len(paths[1]) != 0:
        for alternative_path in paths[1]:
            paths[1].remove(alternative_path)
            floating_string_copy = floating_string[len(alternative_path):]
            for i in floating_string_copy:
                if i.isnumeric():
                    alternative_path += i
                else:
                    new_path = alternative_path + "1"
                    alternative_path += "0"
                    if len(new_path) < 36:
                        paths[1].append(new_path)
                    else:
                        paths[0].append(new_path)
            paths[0].append(alternative_path)

    return paths[0]


def update_memory_slots_version_2():
    instruction_list = copy.deepcopy(compiled_text)
    updated_memory = {}

    for masks in instruction_list.keys():
        for value_pair in instruction_list[masks]:
            decimal_value = value_pair[1]
            decimal_slot = value_pair[0]
            binary_slot = turn_value_into_36_string_binary(decimal_slot)
            all_new_slots = calculate_slots(binary_slot, masks)

            for slot in all_new_slots:
                updated_memory[slot] = decimal_value

    return updated_memory


# while this actually works for these Questions; if I was to change/parse the dictionary(compiled_text) not in the same
# order it was created in this would probably return different values since some key:values in update_memory_slots'
# updated memory are overwritten (also in version 2)
# -> ordered dictionary or just use a regular list instead of a dictionary to solve
print(sum(update_memory_slots().values()))
print(sum(update_memory_slots_version_2().values()))
