import copy

with open("Advent_11_Seats.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(list(line.strip()))


def determine_change(y_pos, x_pos, seating_list):
    character = seating_list[y_pos][x_pos]
    amount_of_surrounding_occupied_seats = 0

    for y, x in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        new_y = y_pos+y
        new_x = x_pos+x
        if 0 <= new_y <= len(seating_list)-1 and 0 <= new_x <= len(seating_list[0])-1:
            if seating_list[new_y][new_x] == "#":
                amount_of_surrounding_occupied_seats += 1

    if character == "L" and amount_of_surrounding_occupied_seats == 0:
        character = "#"
    elif character == "#" and amount_of_surrounding_occupied_seats >= 4:
        character = "L"

    return character


seat_list = copy.deepcopy(compiled_text)
last_seat_list = []

while seat_list != last_seat_list:
    last_seat_list = copy.deepcopy(seat_list)
    for y_position in range(len(last_seat_list)):
        for x_position in range(len(last_seat_list[y_position])):
            seat_list[y_position][x_position] = determine_change(y_position, x_position, last_seat_list)

count = 0
for row in seat_list:
    for thingy in row:
        if thingy == "#":
            count += 1

print(count)


# new rules:
# people care about the next surrounding seat they can see (meaning that if there is an empty space in
# a direction they will overlook it
# for an occupied seat to change back it takes now 5 or more instead of 4 or more surrounding

def determine_change_2(y_pos, x_pos, seating_list):
    character = seating_list[y_pos][x_pos]
    amount_of_surrounding_occupied_seats = 0

    for y, x in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        new_y = y_pos + y
        new_x = x_pos + x
        while True:
            if 0 <= new_y <= len(seating_list)-1 and 0 <= new_x <= len(seating_list[0])-1:
                if seating_list[new_y][new_x] == "#":
                    amount_of_surrounding_occupied_seats += 1
                    break
                elif seating_list[new_y][new_x] == ".":
                    new_y += y
                    new_x += x
                else:
                    break
            else:
                break

    if character == "L" and amount_of_surrounding_occupied_seats == 0:
        character = "#"
    elif character == "#" and amount_of_surrounding_occupied_seats >= 5:
        character = "L"

    return character


seat_list = copy.deepcopy(compiled_text)
last_seat_list = []

while seat_list != last_seat_list:
    last_seat_list = copy.deepcopy(seat_list)
    for y_position in range(len(last_seat_list)):
        for x_position in range(len(last_seat_list[y_position])):
            seat_list[y_position][x_position] = determine_change_2(y_position, x_position, last_seat_list)

count2 = 0
for row in seat_list:
    for thingy in row:
        if thingy == "#":
            count2 += 1

print(count2)
