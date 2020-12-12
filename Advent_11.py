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
