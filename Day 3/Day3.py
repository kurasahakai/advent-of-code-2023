import re

input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

# Find all symbols
symbols_pos = {(r,c): lines[r][c] for r in range(len(lines)) for c in range(len(lines[r])) if lines[r][c] not in "01234567890."}

# Find all numbers
nums = {}
for i, line in enumerate(lines):
    nums[i] = []
    for n in re.finditer(r'\d+', line):
        nums[i].append({(n.start(), n.end()-1): n.group()})

# For each symbol, find if there are numbers with coordinates "touching" the symbol
kernel = [-1, 0, 1]
final_dict = {}
for symbol in symbols_pos:
    symbol_row = symbol[0]
    symbol_index = symbol[1]
    matches = []

    for ker in kernel:
        number_row = symbol_row + ker
        numbers = nums[number_row]

        for num in numbers:
            coords = list(num.keys())[0]
            coords_range = list(range(coords[0], coords[1]+1))
            appeared = False
            for coord in coords_range:
                if coord in [symbol_index-1, symbol_index, symbol_index+1] and not appeared:
                    final_dict[(symbol_row, symbol_index)] = num[coords]
                    matches.append(int(num[coords]))
                    appeared = True

    final_dict[(symbol_row, symbol_index)] = matches

# Part 1
final_list_1 = []
for el in final_dict.values():
    final_list_1.append(el)

flattened_list = [item for sublist in final_list_1 for item in sublist]
parts_sum = sum(flattened_list)


# Part 2 - assuming only cogs have exactly 2 parts numbers
# This can be generalized by checking for symbol in symbols_pos where the value is "*"
final_list_2 = []
for el in final_dict.values():
    if len(el) == 2:
        prod = el[0]*el[1]
        final_list_2.append(prod)

parts_prod = sum(final_list_2)