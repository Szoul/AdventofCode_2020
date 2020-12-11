with open("Advent_8_Console.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(line.strip())


def read_instruction(instr):
    accumulator = 0

    if instr.startswith("jmp"):
        position_increase = int(instr[3:])
    elif instr.startswith("acc"):
        position_increase = 1
        accumulator = int(instr[3:])
    elif instr.startswith("nop"):
        position_increase = 1

    return position_increase, accumulator


def check_acc_at_infinite_loop_start(runtime_list):
    total_acc = 0
    position = 0
    run_history = []

    while position not in run_history:
        instruction = runtime_list[position]
        run_history.append(position)
        next_position, acc = read_instruction(instruction)
        total_acc += acc
        position += next_position

        # for Question 2
        if position == len(runtime_list):
            return total_acc, len(run_history)

    return total_acc, len(run_history)


print(check_acc_at_infinite_loop_start(compiled_text))
print(len(compiled_text))


import copy
already_tested = []
current_test = []

for x in range(len(compiled_text)):
    if compiled_text[x].startswith("nop"):
        current_test = copy.deepcopy(compiled_text)
        current_test[x] = current_test[x].replace("nop", "jmp")
        acc, length = check_acc_at_infinite_loop_start(current_test)
        if length == len(compiled_text):
            break

    elif compiled_text[x].startswith("jmp"):
        current_test = copy.deepcopy(compiled_text)
        current_test[x] = current_test[x].replace("jmp", "nop")
        acc, length = check_acc_at_infinite_loop_start(current_test)
        if length == len(compiled_text):
            break

    else:
        pass

print (acc, length)

