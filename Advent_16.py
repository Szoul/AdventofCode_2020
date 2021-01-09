with open("Advent_16_Tickets.txt", "r") as text_file:
    text_lines = text_file.read()
    rule_lines = text_lines.split("\n\n")[0]
    rule_dict = {}
    for rule_line in rule_lines.split("\n"):
        rule_name = rule_line.split(":")[0]
        rule_ranges = rule_line.split(": ")[1]
        rule_dict[rule_name] = []
        for rule_range in rule_ranges.split(" or "):
            int_rule = []
            for rule in rule_range.split("-"):
                int_rule.append(int(rule))
            rule_dict[rule_name].append(int_rule)

    my_ticket_lines = text_lines.split("\n\n")[1]
    number_line = my_ticket_lines.split("\n")[1]
    my_ticket = []
    for number in number_line.split(","):
        my_ticket.append(int(number))

    nearby_tickets_lines = text_lines.split("\n\n")[2]
    nearby_ticket_list =[]
    for line in nearby_tickets_lines.split("\n")[1:-1]:
        nearby_ticket = []
        for number in line.split(","):
            nearby_ticket.append(int(number))
        nearby_ticket_list.append(nearby_ticket)
# rule_dict = {rule:[[first_range][second_range]], ...}
# my_ticket = list of my ticket information
# nearby_ticket_list = [[ticket_info], ...]


# default returns the scanning error rate (Question 1); discard = True returns nearby_ticket_list with invalids removed
def return_scanning_error_rate(discard=False):
    invalid_numbers = [x for x in range(1000)]
    for values in rule_dict.values():
        for range_list in values:
            for valid_number in range(range_list[0], range_list[1]+1):
                if valid_number in invalid_numbers:
                    invalid_numbers.remove(valid_number)

    scanning_error_rate = 0
    if discard:
        discarded_list = nearby_ticket_list.copy()
    for ticket in nearby_ticket_list:
        valid = True
        for nmb in ticket:
            if nmb in invalid_numbers:
                scanning_error_rate += nmb
                valid = False

        if discard and not valid:
            discarded_list.remove(ticket)

    if discard:
        return discarded_list
    return scanning_error_rate


# Question 2: assume that all tickets returning from return_scanning_error_rate(discard=True) are valid (maybe there is the problem?)
# find out which index of a ticket list corresponds to which field in rule_dict (?)
# return the multiplied numbers of my_ticket that correspond to a rule starting with "departure"

print(rule_dict)
valid_tickets = return_scanning_error_rate(True)
for rule in rule_dict.keys():
    if rule.startswith("departure"):
        rule_ranges = rule_dict[rule]
        first_range = [x for x in range(rule_ranges[0][0], rule_ranges[0][1]+1)]
        second_range = [x for x in range(rule_ranges[1][0], rule_ranges[1][1]+1)]
        total_range = first_range + second_range

        total_indices = [x for x in range(len(my_ticket))]
        corresponding_index = total_indices.copy()
        for current_test_index in total_indices:
            for ticket in nearby_ticket_list:
                number = ticket[current_test_index]
                if number not in total_range:
                    corresponding_index.remove(current_test_index)
                    break

test_rule = "departure location"
test_range = [x for x in range(31, 202)] + [x for x in range(227, 952)]
valid_list = return_scanning_error_rate(discard=True)
invalid = []
for x in range(20):
    for ticket in valid_list:
        number = ticket[x]
        if number not in valid_list:
            invalid.append(x)
            break

# check where it breaks - check if the breaking list is valid at all
