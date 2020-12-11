with open("Advent_9_Preamble.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(int(line.strip()))

for x in range(len(compiled_text)-26):
    previous_25_nums = [compiled_text[z] for z in range(x, x+25)]
    number_to_check = compiled_text[x+25]
    number_works = False

    for w in previous_25_nums:
        for e in previous_25_nums:
            if w != e:
                if w+e == number_to_check:
                    number_works = True

    if not number_works:
        break
print(number_to_check)

array_found = False
array_length = 2
while not array_found:
    for x in range(len(compiled_text)-array_length):
        array = [compiled_text[z] for z in range(x, x+array_length)]
        if sum(array) == number_to_check:
            array_found = True
            break
    array_length += 1

array.sort()
print(array[0]+array[-1])

