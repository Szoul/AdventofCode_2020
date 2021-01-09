with open("Advent_20_Tiles.txt", "r") as text_file:
    text_lines = text_file.readlines()
    tile_dict = {}
    tile = []
    for line in text_lines:
        if line.startswith("Tile"):
            tile_number = int(line.split(" ")[1][:-2])
        elif line == "\n":
            tile_dict[tile_number] = tile
            tile = []
        else:
            tile.append(line.strip())
# tile_dict = {tile_number:[each row of the tile], ...}


# check if two tiles fit on a side (rotating/flipping!)
# it should return a square where the tiles are arranged within -> print(len(tile_dict.keys())) == 144 == 12*12
# return the tile_number of all four corners of that square, multiplied
# since any other tile will have at least 3 adjacent tiles, i need to look for those 4 with only 2 adjacent tiles


def check_if_two_tiles_fit_together(tile_1_number, tile_2_number):
    tile_1_sides = []
    tile_1_flipped_sides = []
    tile_2_sides = []
    for direction in get_sides(tile_1_number):
        tile_1_sides.append(direction)
        tile_1_flipped_sides.append(direction[::-1])
    for direction in get_sides(tile_2_number):
        tile_2_sides.append(direction)

    for side in tile_2_sides:
        if side in tile_1_sides or side in tile_1_flipped_sides:
            adjacent = True
            break
        else:
            adjacent = False

    return adjacent


def get_sides(tile_name):
    left = ""
    right = ""
    for index, row in enumerate(tile_dict[tile_name]):
        if index == 0:
            up = row
        elif index == 9:
            down = row
        left += row[0]
        right += row[-1]

    return up, right, down, left


for test_tile in tile_dict.keys():
    adjacent_counter = 0
    for counter_check_tile in tile_dict.keys():
        if test_tile != counter_check_tile:
            if check_if_two_tiles_fit_together(test_tile, counter_check_tile):
                adjacent_counter += 1

    if adjacent_counter == 2:
        print (test_tile, adjacent_counter)

test_tiles = [3779, 1693, 3677, 1109, 2909, 3371]  # two of these should have 3 sides adjacent (probably) ?


