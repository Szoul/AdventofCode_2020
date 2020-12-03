numbers = []
number_file = open("Advent_1_numbers.txt", "r")
lines = number_file.readlines()
for line in lines:
    numbers.append(int(line.strip()))
number_file.close()


def find_2_that_add_up_to_2020(number_list):
    for x in range(len(number_list)):
        current_number = number_list[x]
        for number in number_list:
            if current_number+number == 2020:
                print(f"{current_number} | {number}")
                print(current_number*number)


def find_3_that_add_up_to_2020(number_list):
    for x in number_list:
        for i in number_list:
            for z in number_list:
                if x+i+z == 2020:
                    print(f"{x} | {i} | {z}")
                    print(x*i*z)


find_2_that_add_up_to_2020(numbers)
print("\n")
find_3_that_add_up_to_2020(numbers)
