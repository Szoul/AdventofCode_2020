with open("Advent_12_Ship.txt", "r") as text_file:
    compiled_text = []
    for line in text_file.readlines():
        compiled_text.append(line.strip())


def execute_instruction(instruction, current_direction):
    directions = ["N", "E", "S", "W"]
    number = int(instruction[1:])

    if instruction.startswith("F"):
        instruction = current_direction

    if instruction.startswith("N"):
        return 0, number, current_direction
    elif instruction.startswith("W"):
        return -number, 0, current_direction
    elif instruction.startswith("E"):
        return number, 0, current_direction
    elif instruction.startswith("S"):
        return 0, -number, current_direction

    else:
        change_direction = number/90
        current_index = directions.index(current_direction)
        if instruction.startswith("L"):
            new_index = int(current_index-change_direction)
        elif instruction.startswith("R"):
            new_index = int(current_index+change_direction)

        if new_index < 0:
            new_index = new_index + 4
        elif new_index > 3:
            new_index = new_index - 4
        current_direction = directions[new_index]
        return 0, 0, current_direction


# first number = East(positive)-West(negative)
# second number = North(positive)-South(negative)
# third entry = position it is currently facing (N = 0/E = 90/S = 180/W = 270)
position = [0, 0, "E"]

for instr in compiled_text:
    y, x, pos = execute_instruction(instr, position[2])
    position[0] += y
    position[1] += x
    position[2] = pos

print(abs(position[0])+abs(position[1]), "\n")


def move_waypoint(instruction, current_waypoint):
    number = int(instruction[1:])
    change = 0, 0

    if instruction.startswith("N"):
        change = 0, number
    elif instruction.startswith("W"):
        change = -number, 0
    elif instruction.startswith("E"):
        change = number, 0
    elif instruction.startswith("S"):
        change = 0, -number

    else:
        if instruction.startswith("L"):
            number = 360-number
        if number == 90:
            current_waypoint = current_waypoint[1], -current_waypoint[0]
        elif number == 180:
            current_waypoint = -current_waypoint[0], -current_waypoint[1]
        elif number == 270:
            current_waypoint = -current_waypoint[1], current_waypoint[0]

    waypoint = [current_waypoint[0]+change[0], current_waypoint[1]+change[1]]
    return waypoint


def move_ship(waypoint, instruction, current_position):
    number = int(instruction[1:])
    moving_distance = waypoint[0]*number, waypoint[1]*number
    new_position = current_position[0]+moving_distance[0], current_position[1]+moving_distance[1]
    return new_position


wp = [10, 1]
position = [0, 0]
for instr in compiled_text:
    if instr.startswith("F"):
        position = move_ship(wp, instr, position)
    else:
        wp = move_waypoint(instr, wp)

print(abs(position[0])+abs(position[1]))