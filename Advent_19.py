import copy

with open("Advent_19_Messages.txt", "r") as text_file:
    text = text_file.read()
    raw_code_rules = text.split("\n\n")[0]
    code_rules = {}
    for line in raw_code_rules.split("\n"):
        key = int(line.split(":")[0])
        all_values = line.split(":")[1]
        code_rules[key] = []
        for possible_message in all_values.split("|"):
            possible_message = possible_message.strip()
            values = []
            for item in possible_message.split(" "):
                if item.isnumeric():
                    values.append(int(item))
                else:
                    values.append(item.strip('"'))
            code_rules[key].append(values)

    raw_messages = text.split("\n\n")[1].strip()
    messages = []
    for line in raw_messages.split("\n"):
        messages.append(line)


# return number of messages that completely match code 0

# replace the number with its contents
# replace each number in contents with its contents
# until the content is a string, then concatenate the strings

# if content has multiple branches - create a new branch - consisting of the new possibility + the unresolved numbers (in right order)
# and reiterate with the above once the first possibility is finished
# until all branches contain strings


def find_all_possible_messages(number):
    pass