from functools import lru_cache

with open("Advent_25_Encryption.txt", "r") as text_file:
    text_lines = text_file.readlines()
    public_key_one = int(text_lines[0].strip())
    public_key_two = int(text_lines[1].strip())


def get_loop_size(public_key):
    subject_number = 7
    loop_size = 0
    value = 1
    while value != public_key:
        loop_size += 1
        value *= subject_number
        value = value % 20201227

    return loop_size


def get_encryption_key(public_key, loop_size):
    subject_number = public_key
    value = 1
    for x in range(loop_size):
        value *= subject_number
        value = value % 20201227

    return value


def open_sesame(first_public_key, second_public_key):
    size_of_loop_first = get_loop_size(first_public_key)
    encryption_key = get_encryption_key(second_public_key, size_of_loop_first)

    return encryption_key


print (open_sesame(public_key_one, public_key_two))
print (open_sesame(public_key_two, public_key_one))
