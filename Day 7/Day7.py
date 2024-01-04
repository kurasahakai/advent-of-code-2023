from collections import Counter

input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

card_str = {"A":14,
            "K":13,
            "Q":12,
            "J":11,
            "T":10,
            "9":9,
            "8":8,
            "7":7,
            "6":6,
            "5":5,
            "4":4,
            "3":3,
            "2":2}

hands_str = {"five_of_a_kind":7,
             "four_of_a_kind":6,
             "full_house":5,
             "three_of_a_kind":4,
             "two_pairs":3,
             "pair":2,
             "high_card":1}

# Part 1
def hand_str(hand):
    cards = list(hand)
    hand_dict = Counter(cards)

    if 5 in hand_dict.values():
        hand_type = "five_of_a_kind"
    elif 4 in hand_dict.values():
        hand_type = "four_of_a_kind"
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        hand_type = "full_house"
    elif 3 in hand_dict.values():
        hand_type = "three_of_a_kind"
    elif len([x for x in hand_dict.values() if x == 2]) == 2:
        hand_type = "two_pairs"
    elif 2 in hand_dict.values():
        hand_type = "pair"
    else:
        hand_type = "high_card"

    return hand_type

hands_bids = {}
for line in lines:
    hand = line.split(" ")[0]
    bid = int(line.split(" ")[1])

    hands_bids.update({hand: bid})

hands = []
for hand in hands_bids:
    hand_type = hand_str(hand)
    cards = list(hand)
    hands.append((hand, hands_bids[hand], hands_str[hand_type] ,hand_type, card_str[cards[0]], card_str[cards[1]],card_str[cards[2]], card_str[cards[3]], card_str[cards[4]]))

sorted_hands = sorted(hands, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

values = []
for n, hand in enumerate(sorted_hands):
    value = (n+1)*hand[1]
    values.append(value)

sum_values = sum(values)

# Part 2
card_str = {"A":14,
            "K":13,
            "Q":12,
            "J":1,
            "T":10,
            "9":9,
            "8":8,
            "7":7,
            "6":6,
            "5":5,
            "4":4,
            "3":3,
            "2":2}

def hand_str_w_J(hand):
    cards = list(hand)
    if "J" not in cards:
        hand_dict = Counter(cards)

        if 5 in hand_dict.values():
            hand_type = "five_of_a_kind"
        elif 4 in hand_dict.values():
            hand_type = "four_of_a_kind"
        elif 3 in hand_dict.values() and 2 in hand_dict.values():
            hand_type = "full_house"
        elif 3 in hand_dict.values():
            hand_type = "three_of_a_kind"
        elif len([x for x in hand_dict.values() if x == 2]) == 2:
            hand_type = "two_pairs"
        elif 2 in hand_dict.values():
            hand_type = "pair"
        else:
            hand_type = "high_card"

    if "J" in cards:
        best_value = 0

        for card in card_str:
            new_hand = list(map(lambda x: x.replace("J", card), hand))
            hand_dict = Counter(new_hand)

            if 5 in hand_dict.values():
                hand_type = "five_of_a_kind"
            elif 4 in hand_dict.values():
                hand_type = "four_of_a_kind"
            elif 3 in hand_dict.values() and 2 in hand_dict.values():
                hand_type = "full_house"
            elif 3 in hand_dict.values():
                hand_type = "three_of_a_kind"
            elif len([x for x in hand_dict.values() if x == 2]) == 2:
                hand_type = "two_pairs"
            elif 2 in hand_dict.values():
                hand_type = "pair"
            else:
                hand_type = "high_card"

            value = hands_str[hand_type]
            if value > best_value:
                best_value = value
                best_type = hand_type

        hand_type = best_type
    return hand_type


hands = []
for hand in hands_bids:
    hand_type = hand_str_w_J(hand)
    cards = list(hand)
    hands.append((hand, hands_bids[hand], hands_str[hand_type] ,hand_type, card_str[cards[0]], card_str[cards[1]],card_str[cards[2]], card_str[cards[3]], card_str[cards[4]]))

sorted_hands = sorted(hands, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

values = []
for n, hand in enumerate(sorted_hands):
    value = (n+1)*hand[1]
    values.append(value)

sum_values = sum(values)