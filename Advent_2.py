import re

password_file = open("Advent_2_Passwords.txt", "r")
list_of_each_line = []
for line in password_file.readlines():
    list_of_each_line.append(line.strip())
password_file.close()

regex = re.compile(r"""
                   (^\d*?)
                   -
                   (\d*?)
                   \s
                   (\w)
                   :\s
                   (\w*$)
                   """, re.VERBOSE)


def first_exercise(list_of_lines):
    number_of_right_passwords = 0
    for password_line in list_of_lines:
        res = regex.match(password_line)
        first_number = res.group(1)
        second_number = res.group(2)
        letter = res.group(3)
        password = res.group(4)

        number_of_letters_in_password = 0
        for single_letter in password:
            if single_letter == letter:
                number_of_letters_in_password += 1

        if int(first_number) <= number_of_letters_in_password <= int(second_number):
            number_of_right_passwords += 1

    return number_of_right_passwords


def second_exercise(list_of_lines):
    number_of_right_passwords = 0
    for password_line in list_of_lines:
        res = regex.match(password_line)
        first_number = int(res.group(1))
        second_number = int(res.group(2))
        letter = res.group(3)
        password = res.group(4)

        if (password[first_number - 1] == letter and password[second_number - 1] != letter) or (
                password[first_number - 1] != letter and password[second_number - 1] == letter):
            number_of_right_passwords += 1

    return number_of_right_passwords


print(first_exercise(list_of_each_line))
print("\n")
print(second_exercise(list_of_each_line))
