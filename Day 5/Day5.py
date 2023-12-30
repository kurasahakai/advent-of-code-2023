input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
for line in lines:
    if line == "":
        lines.remove(line)

seeds_n = lines[0].split(": ")[1].split(" ")
seeds_n = [int(seed) for seed in seeds_n]

maps_names = [line for line in lines if "map" in line]

# Creating a dictionary with maps and their values
map_data = {}
current_map = None
values = []
for item in lines:
    if item in maps_names:
        if current_map:
            map_data[current_map] = values
        current_map = item
        values = []
    else:
        values.append(item)

if current_map:
    map_data[current_map] = values

# Part 1
for map in map_data:
    ranges = []
    for x in map_data[map]:
        items = x.split(" ")
        items = [int(item) for item in items]
        ranges.append(items)

    locs = []
    for seed in seeds_n:
        for item in ranges:
            if seed in range(item[1], item[1]+item[2]):
                locs.append(seed - item[1] + item[0])
                break
        else:
            locs.append(seed)

    seeds_n = locs # This moves the process one step down the line
print(min(locs))

# Part 2
seeds_n = lines[0].split(": ")[1].split(" ")
seeds_n = [int(seed) for seed in seeds_n]

seeds = []
for i in range(0, len(seeds_n), 2):
    seeds.append((seeds_n[i], seeds_n[i] + seeds_n[i + 1]))

for map in map_data:
    ranges = []
    for x in map_data[map]:
        items = x.split(" ")
        items = [int(item) for item in items]
        ranges.append(items)

    locs = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for item in ranges:
            overlap_start = max(start, item[1])
            oe = min(end, item[1] + item[2])
            if overlap_start < oe:
                locs.append((overlap_start - item[1] + item[0], oe - item[1] + item[0]))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > oe:
                    seeds.append((oe, end))
                break
        else:
            locs.append((start, e))
    seeds = locs

print(min(seeds)[0])