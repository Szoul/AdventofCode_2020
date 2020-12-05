import copy, re

with open("Advent_4_Batch.txt", "r") as text_file:
    text = text_file.read()
    text_list = text.split("\n\n")

expected_entries = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

text_list_with_invalids_removed = copy.deepcopy(text_list)
for passport in text_list:
    for entry in expected_entries:
        if entry not in passport:
            text_list_with_invalids_removed.remove(passport)
            break

print(len(text_list_with_invalids_removed))


compiled_text = []
for passport in text_list_with_invalids_removed:
    chunks = passport.split()
    passport_dict = {}
    for chunk in chunks:
        passport_dict[chunk.split(":")[0]] = chunk.split(":")[1]
    compiled_text.append(passport_dict)

list_of_valid_passports_2 = []
for passport in compiled_text:
    if not 1920 <= int(passport["byr"]) <= 2002:
        continue

    if not 2010 <= int(passport["iyr"]) <= 2020:
        continue

    if not 2020 <= int(passport["eyr"]) <= 2030:
        continue

    if passport["hgt"].endswith("cm"):
        if 150 <= int(passport["hgt"][:-2]) <= 193:
            pass
        else:
            continue
    elif passport["hgt"].endswith("in"):
        if 59 <= int(passport["hgt"][:-2]) <= 76:
            pass
        else:
            continue
    else:
        continue

    hcl_regex = re.compile(r"[#][0-9,a-f]{6}")
    if not hcl_regex.fullmatch(passport["hcl"]):
        continue

    ecl_matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if passport["ecl"] not in ecl_matches:
        continue

    if passport["pid"].isdigit() and len(passport["pid"]) == 9:
        pass
    else:
        continue

    list_of_valid_passports_2.append(passport)

print(len(list_of_valid_passports_2))