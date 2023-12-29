input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

# Max number of cubes available per color
max_red = 12
max_green = 13
max_blue = 14

# Part 1
impossible_ids = []
ids = []
for line in lines:
    game_id = line.split(":")[0].split(" ")[1]
    ids.append(game_id)
    pulls = line.split(":")[1].split(";")

    for pull in pulls:
        dices = pull.split(",")
        red, green, blue = 0, 0, 0

        for dice in dices:
            if "red" in dice:
                red = int(dice.split(" ")[1])
            elif "blue" in dice:
                blue = int(dice.split(" ")[1])
            elif "green" in dice:
                green = int(dice.split(" ")[1])

            if red > max_red or blue > max_blue or green > max_green:
                impossible_ids.append(game_id)

possible_ids = [id for id in ids if id not in impossible_ids]
possible_ids_sum = sum([int(id)for id in possible_ids])

# Part 2
powers = []
for line in lines:
    games = line.split(":")[1].split(";")
    red, green, blue = 0, 0, 0
    for game in games:
        dices = game.split(",")

        for dice in dices:
            # Find the amount of dices per each color, if this is greater than the max, replace it
            if "red" in dice:
                red_n = int(dice.split(" ")[1])
                if red_n > red:
                    red = red_n

            elif "blue" in dice:
                blue_n = int(dice.split(" ")[1])
                if blue_n > blue:
                    blue = blue_n

            elif "green" in dice:
                green_n = int(dice.split(" ")[1])
                if green_n > green:
                    green = green_n
    powers.append(green*red*blue)
powers_sum = sum(powers)