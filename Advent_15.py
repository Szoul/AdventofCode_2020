from collections import deque, defaultdict
import time

my_input = [7, 14, 0, 17, 11, 1, 2]


def get_next_number(number_list):

    for position, number in reversed(list(enumerate(number_list))):
        if position == len(number_list)-1:
            last_number = number
            last_position = position
            continue
        elif number == last_number:
            difference = last_position - position
            return difference
        elif position == 0 and number != last_number:
            return 0


def get_number_at_goal_index(original_input, goal_length):
    deque_dict = defaultdict(deque)
    for index, value in enumerate(original_input):
        deque_dict[value].append(index+1)

    last_number = original_input[-1]
    next_index = index+1

    while next_index != goal_length:

        if len(deque_dict[last_number]) == 1:
            next_number = 0
        else:
            next_number = next_index - deque_dict[last_number][0]

        next_index += 1
        deque_dict[next_number].append(next_index)
        if len(deque_dict[next_number]) == 3:
            deque_dict[next_number].popleft()
        last_number = next_number

    return last_number


# first attempt
while len(my_input) != 2020:
    my_input.append(get_next_number(my_input))

print(my_input[-1])

# second attempt
num = get_number_at_goal_index(my_input[:7], 30000000)
print(num)  # 955 for my input
