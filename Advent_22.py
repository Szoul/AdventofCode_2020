import copy

with open("Advent_22_Crabs.txt", "r") as text_file:
    first_player = []
    second_player = []
    text_lines = text_file.readlines()
    parse_second_player = False
    for line in range(len(text_lines)):
        if not parse_second_player:
            if text_lines[line] == "Player 1:\n":
                continue
            elif text_lines[line] == "\n":
                parse_second_player = True
                continue
            else:
                first_player.append(int(text_lines[line].strip()))
        elif parse_second_player:
            if text_lines[line] == "Player 2:\n":
                continue
            else:
                second_player.append(int(text_lines[line].strip()))


def play_round(first, second):
    if first[0] > second[0]:
        first.append(first[0])
        first.append(second[0])
    elif first[0] < second[0]:
        second.append(second[0])
        second.append(first[0])

    first.remove(first[0])
    second.remove(second[0])

    return first, second


def play_game():
    fp = copy.deepcopy(first_player)
    sp = copy.deepcopy(second_player)
    while len(fp) != 0 and len(sp) != 0:
        fp, sp = play_round(fp, sp)

    if len(fp) != 0:
        return fp
    else:
        return sp


def evaluate_score(player_list):
    player_list.reverse()
    total_score = 0
    for x in range(len(player_list)):
        total_score += (x+1)*player_list[x]
    return total_score


print(evaluate_score(play_game()))


def play_but_in_recursive(first_p, second_p):
    game_states = []
    game_round = 0
    while True:
        # check if game state has existed before to stop infinite loops
        current_state = [first_p.copy(), second_p.copy()]
        if current_state in game_states:
            winner = first_p
            break
        else:
            game_states.append(current_state)

        # check if one player has run out of cards
        if len(first_p) == 0:
            winner = second_p
            break
        elif len(second_p) == 0:
            winner = first_p
            break
        else:
            # check if there needs to be a sub-game to determine the winner
            if first_p[0] <= len(first_p)-1 and second_p[0] <= len(second_p)-1:
                recursive_deck_first = first_p[1:first_p[0]+1]
                recursive_deck_second = second_p[1:second_p[0]+1]
                sub_game_winner, unused = play_but_in_recursive(recursive_deck_first, recursive_deck_second)
                if sub_game_winner == 1:
                    first_p.append(first_p[0])
                    first_p.append(second_p[0])
                elif sub_game_winner == 2:
                    second_p.append(second_p[0])
                    second_p.append(first_p[0])
                first_p.remove(first_p[0])
                second_p.remove(second_p[0])

            # otherwise just calculate the round's winner by highest number
            else:
                first_p, second_p = play_round(first_p, second_p)

        game_round += 1

    if winner == first_p:
        return 1, winner
    elif winner == second_p:
        return 2, winner


winning_player, their_deck = play_but_in_recursive(first_player, second_player)
print(evaluate_score(their_deck), winning_player)
