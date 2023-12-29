input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

# Part 1
digits = []
for line in lines:
    first_digit = last_digit = None
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = int(char)
            last_digit = int(char)

    digits.append(str(first_digit)+str(last_digit))

digits = [int(digit) for digit in digits]
digits_sum = sum(digits)

# Part 2
import re

numbers_map = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

digits_2 = []

for line in lines:
    found = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    first_digit = found[0]
    first_digit = numbers_map.get(first_digit, first_digit)

    last_digit = found[-1]
    last_digit = numbers_map.get(last_digit, last_digit)

    digits_2.append(str(first_digit) + str(last_digit))

digits_2 = [int(digit) for digit in digits_2]
digits_sum_2 = sum(digits_2)