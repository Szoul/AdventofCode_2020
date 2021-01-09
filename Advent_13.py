import math
from functools import reduce

with open("Advent_13_Bus.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = [text_lines[0].strip(), []]
    compiled_text[1] = text_lines[1].strip().split(",")


def part1():
    time = int(compiled_text[0])
    lowest_time = 100
    for bus in compiled_text[1]:
        if bus != "x":
            bus = int(bus)
            next_stop = math.ceil(time/bus)
            time_to_wait = next_stop*bus-time

            if lowest_time > time_to_wait:
                next_bus = bus
                lowest_time = time_to_wait

    print(lowest_time * next_bus)


bus_position_dict = {}
for i in range(len(compiled_text[1])):
    if compiled_text[1][i] != "x":
        bus_position_dict[int(compiled_text[1][i])] = i


def chinese_remainder_theorem(bus_dict):    # dict of {mod:remainder, ...} or {bus:time after t, ...}
    product_of_moduli = reduce((lambda x, y: x*y), bus_dict.keys())
    total = 0
    for mod in bus_dict.keys():
        remainder = bus_dict[mod]
        new_mod = product_of_moduli / mod
        inverse_remainder = new_mod % mod
        inverse = 1
        while (inverse_remainder*inverse) % mod != 1:
            inverse += 1

        product = remainder*new_mod*inverse
        total += product

    lowest_congruent_number = total % product_of_moduli

    return int(lowest_congruent_number)

print (bus_position_dict)


def part2():
    bus_list = list(bus_position_dict.keys()).copy()
    arrival_list = []
    for item in bus_list:
        arrival_list.append(bus_position_dict[item])


    iterations = 0
    offset = 0
    x = 0
    multiple = bus_list[x]
    for x in range(len(bus_list)-1):
        while True:
            if (offset+multiple*iterations) % bus_list[x+1] != arrival_list[x+1]:
                iterations += 1
            else:
                offset = offset + iterations * multiple
                multiple *= bus_list[x+1]
                iterations = 0
                break

