my_input = "784235916"

cups = []
for number in my_input:
    cups.append(int(number))


def play_crab_cups(rounds, cup_list):
    c_list = cup_list.copy()
    current_cup = c_list[0]
    lowest_cup = min(c_list)
    highest_cup = max(c_list)

    for x in range(rounds):
        # rearrange list so that the first cup == current_cup (will only loop once, might as well use an if statement)
        while current_cup != c_list[0]:
            cup_to_move = c_list[0]
            c_list.remove(c_list[0])
            c_list.append(cup_to_move)

        cups_to_move = c_list[1:4]

        # calculate the destination_cup
        destination_cup = current_cup
        while True:
            destination_cup -= 1
            if destination_cup < lowest_cup:
                destination_cup = highest_cup
            if destination_cup not in cups_to_move and destination_cup in c_list:
                break

        # move cups_to_move after the destination cup
        destination_index = c_list.index(destination_cup)
        for cup in cups_to_move:
            c_list.remove(cup)
            c_list.insert(destination_index, cup)

        # assign the next cup after current_cups as the new current_cup
        current_cup = c_list[1]

    return c_list


def get_order_after_cup_1(cup_list):
    c_list = cup_list.copy()
    cup_1 = c_list[c_list.index(1)]
    while cup_1 != c_list[0]:
        cup_to_move = c_list[0]
        c_list.remove(c_list[0])
        c_list.append(cup_to_move)

    order = ""
    for nmb in c_list[1:]:
        order += str(nmb)

    return order


for x in range(100):
    print (play_crab_cups(x, cups))
print(get_order_after_cup_1(play_crab_cups(100, cups)))

# Question 2
# initial list =  original list, but (highest number +1) appended until 1 million numbers in list
# ten million moves
# what are the two numbers after 1 (clockwise) after those moves multiplied?
    # if i dont sort the lsit for the cuurent cup at 1
    # the current cup will always be at the index of the last cup +1

# circular linked lists
from collections import deque
