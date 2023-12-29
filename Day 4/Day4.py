import re

input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

cards_dict = {}
for card in lines:
    card_n = re.findall(r"\d+", card.split(":")[0])[0]
    winning_ns = re.findall(r"\d+",card.split(": ")[1].split(" |")[0])
    my_ns = re.findall(r"\d+",card.split("| ")[1])

    wins = []
    for n in my_ns:
        if n in winning_ns:
            wins.append(n)

    cards_dict[card_n] = wins

# Part 1
points_list = []
for card in cards_dict.values():
    if len(card)>0:
        points = 2**(len(card)-1)
        points_list.append(points)

points_tot = sum(points_list)

cards_dict = {}
for card in lines:
    card_n = re.findall(r"\d+", card.split(":")[0])[0]
    winning_ns = re.findall(r"\d+",card.split(": ")[1].split(" |")[0])
    my_ns = re.findall(r"\d+",card.split("| ")[1])

    wins = []
    for n in my_ns:
        if n in winning_ns:
            wins.append(n)

    cards_dict[card_n] = wins

# Part 2
n_wins_dict = {}
for card in cards_dict:
    n_wins_dict[int(card)] = len(cards_dict[card])

num_cards = {int(card): 1 for card in n_wins_dict}
for card in num_cards:
    card_copies = num_cards[card]
    numbers_cards_won = n_wins_dict[card]

    for i in range(1, numbers_cards_won+1):
        new_card = card+i
        num_cards[new_card] += card_copies

total_n_cards = sum(list(num_cards.values()))