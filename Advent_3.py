line_list = []
text_file = open("Advent_3_Trees.txt", "r")
for line in text_file.readlines():
    line = line.replace("\n", "")
    line_list.append(line)
text_file.close()


def counting_trees(list_of_lines, x_counter, y_counter):
    x_axis_length = len(list_of_lines[0])
    tree_count = 0
    x_axis = 0
    for y_axis in range(len(list_of_lines)):
        if y_axis % y_counter == 0:
            if list_of_lines[y_axis][x_axis] == "#":
                tree_count += 1

        x_axis += x_counter
        if x_axis >= x_axis_length:
            x_axis = x_axis-x_axis_length

    return tree_count


multiplied_number = 1
for x, y in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
    print(counting_trees(line_list, x, y))
    multiplied_number *= counting_trees(line_list, x, y)
print(multiplied_number)
