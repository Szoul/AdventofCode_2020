import copy

with open("Advent_11_Seats.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(list(line.strip()))


def determine_change(y_position, x_position, seat_list):
    character = seat_list[y_position][x_position]
    amount_of_surrounding_occupied_seats = 0

    for y, x in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        try:
            if seat_list[y_position+y][x_position+x] == "#":
                amount_of_surrounding_occupied_seats += 1
        except IndexError:
            continue

    if character == "L" and amount_of_surrounding_occupied_seats == 0:
        character = "#"
    elif character == "#" and amount_of_surrounding_occupied_seats >= 4:
        character = "L"

    return character


current_seats = copy.deepcopy(compiled_text)
while True:
    last_seat_distribution = copy.deepcopy(current_seats)

    for y_pos in range(len(last_seat_distribution)):
        for x_pos in range(len(last_seat_distribution[y_pos])):
            current_seats[y_pos][x_pos] = determine_change(y_pos, x_pos, last_seat_distribution)

    if last_seat_distribution == current_seats:
        break

total_occupied_amount = 0
for line in current_seats:
    print(line)
    for place in line:
        if place == "#":
            total_occupied_amount += 1

print(total_occupied_amount)
