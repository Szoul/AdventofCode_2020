import re

with open("Advent_18_Homework.txt", "r") as text_file:
    text_lines = text_file.readlines()
    compiled_text = []
    for line in text_lines:
        compiled_text.append(line.strip().replace(" ", ""))

first_expression_regex = re.compile(r"(^\d+.\d+)")
plus_expression_regex = re.compile(r"(\d+\+\d+)")


# Question 1
def evaluate_expression_without_parenthesis_left_to_right(string_expression):
    if string_expression.isnumeric():
        return int(string_expression)
    else:
        match = first_expression_regex.match(string_expression)
        string_to_evaluate = match.group()
        res = eval(string_to_evaluate)
        new_expression = string_expression.replace(string_to_evaluate, str(res), 1)
        evaluation = evaluate_expression_without_parenthesis_left_to_right(new_expression)
        return str(evaluation)


# Question 2
def evaluate_expression_without_parenthesis_prioritizing_plus(string_expression):
    if string_expression.isnumeric():
        return str(string_expression)
    else:
        if "+" in string_expression:
            match = plus_expression_regex.search(string_expression)
            string_to_evaluate = match.group()
            res = eval(string_to_evaluate)
            new_expression = string_expression.replace(string_to_evaluate, str(res), 1)
            evaluation = evaluate_expression_without_parenthesis_prioritizing_plus(new_expression)
            return str(eval(evaluation))
        else:
            return str(eval(string_expression))


def evaluate_expression(string_expression, question=1):
    if "(" in string_expression:
        smallest_difference = 1000
        for x in range(len(string_expression)):
            if string_expression[x] == ")":
                closing_bracket = x
                break
        for y in range(len(string_expression)):
            if string_expression[y] == "(":
                if 0 < closing_bracket-y < smallest_difference:
                    smallest_difference = closing_bracket-y
                    opening_bracket = y

        expression = string_expression[opening_bracket+1:closing_bracket]
        if question == 1:
            evaluated_expression = evaluate_expression_without_parenthesis_left_to_right(expression)
            new_string = string_expression[:opening_bracket] + evaluated_expression + string_expression[
                                                                                      closing_bracket + 1:]
            final_result = evaluate_expression(new_string)
        else:
            evaluated_expression = evaluate_expression_without_parenthesis_prioritizing_plus(expression)
            new_string = string_expression[:opening_bracket] + evaluated_expression + string_expression[
                                                                                      closing_bracket + 1:]
            final_result = evaluate_expression(new_string, 2)

        return final_result

    else:
        if question == 1:
            return int(evaluate_expression_without_parenthesis_left_to_right(string_expression))
        else:
            return int(evaluate_expression_without_parenthesis_prioritizing_plus(string_expression))


total_number = 0
for line in compiled_text:
    result = evaluate_expression(line)
    total_number += result

print(total_number)

total_number_2 = 0
for line in compiled_text:
    result = evaluate_expression(line, 2)
    total_number_2 += result

print(total_number_2)