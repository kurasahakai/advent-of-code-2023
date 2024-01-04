import re
import math as m

input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

durations = re.findall(r"\d+", lines[0])
distances = re.findall(r"\d+", lines[1])

# Part 1
wins = []
for race in range(len(distances)):
    race_duration = int(durations[race])
    race_record = int(distances[race])

    couples_list = [(i, race_duration - i) for i in range(race_duration + 1)]

    winning_races = []
    for strategy in couples_list:
        press = strategy[0]
        release = strategy[1]

        distance_raced = press*release
        if distance_raced > race_record:
            winning_races.append(strategy)

    wins.append(len(winning_races))

product_wins = m.prod(wins)

# Part 2
# One way to solve this analytically would be to find the minimum integer K such that
# K*duration > distance. distance - 2 K should give us the correct number

distance = int("".join(distances))
duration = int("".join(durations))

couples_list = [(i, duration - i) for i in range(duration + 1)]

winning_races = []
for strategy in couples_list:
    press = strategy[0]
    release = strategy[1]

    distance_raced = press*release
    if distance_raced>distance:
        winning_races.append(strategy)
