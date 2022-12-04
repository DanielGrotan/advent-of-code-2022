with open("input.txt") as file:
    strategy_guide = file.read()

turn_strategies = strategy_guide.splitlines()

choice_map = {"A": 1, "B": 2, "C": 3, "rock": 1, "paper": 2, "scissors": 3}
result_map = {"X": 0, "Y": 3, "Z": 6}

total_score = 0
for turn_strategy in turn_strategies:
    opponent_choice, result = turn_strategy.split(" ")

    result_score = result_map[result]

    match (opponent_choice, result):
        case ("A", "Y") | ("B", "X") | ("C", "Z"):
            choice_score = choice_map["rock"]
        case ("A", "Z") | ("B", "Y") | ("C", "X"):
            choice_score = choice_map["paper"]
        case ("A", "X") | ("B", "Z") | ("C", "Y"):
            choice_score = choice_map["scissors"]

    turn_score = result_score + choice_score

    total_score += turn_score

print(total_score)
