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

        # for Question 2
        if instruction == "Goodbye, and thanks for all the fish":
            return "finished", total_acc

        run_history.append(position)
        next_position, acc = read_instruction(instruction)
        total_acc += acc
        position += next_position

    return total_acc, len(run_history)


print(check_acc_at_infinite_loop_start(compiled_text)[0])


# 2: change one item "nop" to "jmp" or the other way round, so that the line after the last line would be reached
import copy

compiled_text.append("Goodbye, and thanks for all the fish")

for x in range(len(compiled_text)):
    test = copy.deepcopy(compiled_text)
    if test[x].startswith("nop"):
        test[x] = "jmp"+test[x][3:]
    elif test[x].startswith("jmp"):
        test[x] = "nop" + test[x][3:]

    finish_comment, acc = check_acc_at_infinite_loop_start(test)
    if finish_comment == "finished":
        break

print(acc)


