with open("Advent_24_Tiles.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(line.strip())


# Question 1
def get_coordinate(text_instruction):
    instr = text_instruction
    key_list = ["e", "w", "ne", "nw", "se", "sw"]
    value_list = [[1, 1, 0], [-1, -1, 0], [0, 1, 1], [-1, 0, 1], [1, 0, -1], [0, -1, -1]]
    coordinate_dict = dict(zip(key_list, value_list))
    coordinate = [0, 0, 0]
    while len(instr) != 0:
        current_instruction = instr[0]
        if current_instruction != "e" and current_instruction != "w":
            current_instruction = instr[0:2]
        instr = instr.replace(current_instruction, "", 1)
        current_instruction = coordinate_dict[current_instruction]

        coordinate = [coordinate[i] + current_instruction[i] for i in range(len(coordinate))]

    return coordinate


def calculate_black_tiles():
    black_tiles = []
    for command in compiled_text:
        cod = get_coordinate(command)
        if cod not in black_tiles:
            black_tiles.append(cod)
        else:
            black_tiles.remove(cod)
    return black_tiles


# Question 2
def check_and_change_colour_list(tile, num_of_surrounding_black_tiles, black_tile_list):
    global list_of_parsed_tiles
    global changing_tile_list
    if tile not in list_of_parsed_tiles:
        if tile not in black_tile_list and num_of_surrounding_black_tiles == 2:
            # tile becomes black -> append to a new list
            changing_tile_list.append(tile)
        elif tile in black_tile_list and (num_of_surrounding_black_tiles == 0 or num_of_surrounding_black_tiles > 2):
            # tile becomes white -> append to new list and later remove when the tile also is in the old list
            changing_tile_list.append(tile)
        else:
            # tile stays the way it is -> when comparing to old list it will append since it wont appear double
            pass
        list_of_parsed_tiles.append(tile)


def change_colour_of_tile_and_its_surrounding(tile, black_tile_list, recursion=0):
    # check a tile and its surrounding tiles (recursion=1) if they are about to change via the above function
    surrounding = [[1, 1, 0], [1, 0, -1], [0, -1, -1], [-1, -1, 0], [-1, 0, 1], [0, 1, 1]]
    number_of_black_tiles = 0

    for tile_directions in surrounding:
        surrounding_coordinate = [tile_directions[i] + tile[i] for i in range(len(tile))]

        if recursion == 0:
            change_colour_of_tile_and_its_surrounding(surrounding_coordinate, black_tile_list, recursion=1)

        if surrounding_coordinate in black_tile_list:
            number_of_black_tiles += 1

    check_and_change_colour_list(tile, number_of_black_tiles, black_tile_list)


list_of_parsed_tiles = []
changing_tile_list = []


def get_black_tiles_after_x_days(number_of_days):
    old_black_tile_list = calculate_black_tiles().copy()
    global list_of_parsed_tiles
    global changing_tile_list
    for day in range(number_of_days):
        print(f"Calculating Day: {day+1}")
        list_of_parsed_tiles = []
        changing_tile_list = []

        # fill changing_tile_list with all tiles that are changing (either colour)
        for black_tile in old_black_tile_list:
            change_colour_of_tile_and_its_surrounding(black_tile, old_black_tile_list, recursion=0)

        # counter-check the new with the old list and remove all duplicates, add all new entries
        new_list = []
        for black_tile in old_black_tile_list:
            if black_tile not in changing_tile_list:
                new_list.append(black_tile)
        for black_tile in changing_tile_list:
            if black_tile not in old_black_tile_list:
                new_list.append(black_tile)
        old_black_tile_list = new_list.copy()

    return old_black_tile_list


print(len(calculate_black_tiles()))
# Took about 17-18 min on my old pc, definitely could use some optimisation, but it works (solution to my input: 4118)
print(len(get_black_tiles_after_x_days(100)))
