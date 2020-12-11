with open("Advent_10_Adapters.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(int(line.strip()))
    compiled_text.append(0)
    compiled_text.sort()
    compiled_text.append(compiled_text[-1]+3)

number_of_1_jolts = 0
number_of_2_jolts = 0
number_of_3_jolts = 0
for x in range(1, len(compiled_text)):
    difference = compiled_text[x]-compiled_text[x-1]
    if difference == 1:
        number_of_1_jolts += 1
    elif difference == 2:
        number_of_2_jolts += 1
    elif difference == 3:
        number_of_3_jolts += 1

print(number_of_1_jolts*number_of_3_jolts)
print(compiled_text)


# if the difference between two numbers is 3 than there is only one possible permutation for this
# anything in between can be treated as independent permutations (multiply for goal)
# possibilities are equal to the numbers in the tribonachi sequence ([0,0]1,1,2,4,7,13,24,...)
# there are no more than four consecutive numbers that differ by 1 in a row

# another way: convert the list into a list of the changed amount [1-1-3-1-3-3-1-1-1-1-3-1-...]
# calculate the "possibilities" of reaching the next 3 - multiplied for whole list


def permutation_possibilities(number):
    tribonachi = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    return tribonachi[number]


total_permutation_possibilities = 1
current_permutation = 0
for x in compiled_text:
    if x+1 in compiled_text:
        current_permutation += 1
    elif x+3 in compiled_text:
        total_permutation_possibilities *= permutation_possibilities(current_permutation)
        current_permutation = 0

print(total_permutation_possibilities)
