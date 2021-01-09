with open("Advent_17_AnotherConway.txt", "r") as text_file:
    text_lines = text_file.readlines()
    original_grid = []
    for y_coordinate in range(len(text_lines)):
        for x_coordinate in range(len(text_lines[y_coordinate])):
            if text_lines[y_coordinate][x_coordinate] == "#":
                original_grid.append([x_coordinate, y_coordinate, 0])


def change_active_nodes(activated_node, active_node_list, recursion=0):
    global parsed_memory
    global new_grid
    node = activated_node.copy()
    number_of_surrounding_active_nodes = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            for z in (-1, 0, 1):
                if x == 0 and y == 0 and z == 0:
                    pass
                else:
                    neighbour_node = [node[i] + [x, y, z][i] for i in range(len(node))]
                    if recursion == 0 and neighbour_node not in parsed_memory:
                        change_active_nodes(neighbour_node, active_node_list, recursion=1)

                    if neighbour_node in active_node_list:
                        number_of_surrounding_active_nodes += 1

    if node not in parsed_memory:
        if node not in active_node_list and number_of_surrounding_active_nodes == 3:
            new_grid.append(node)
        elif node in active_node_list and 2 <= number_of_surrounding_active_nodes <= 3:
            new_grid.append(node)
        else:
            pass

        parsed_memory.append(node)


current_grid = original_grid.copy()
for cycles in range(6):
    parsed_memory = []
    new_grid = []
    # go through each active node and check if it or one of it surrounding nodes will change next iteration
    # save next iteration in <new_grid> and nodes that have already been accounted for in <parsed_memory>
    for active_node in original_grid:
        change_active_nodes(active_node, current_grid)

    current_grid = new_grid

print(len(current_grid))
