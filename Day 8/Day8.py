input_file = "input.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
for line in lines:
    if line == "":
        lines.remove(line)

instructions = lines[0]
nodes = lines[1:]

couples = {}
for node in nodes:
    node_name = node.split(" = ")[0]
    node_directions_1 = node.split("(")[1].split(",")[0]
    node_directions_2 = node.split("(")[1].split(", ")[1].split(")")[0]

    couples.update({node_name:(node_directions_1, node_directions_2)})

#  Part 1
start = "AAA"
arrived = False
steps = 0
instruction_counter = 0

while not arrived:
   new_coords = couples[start]
   try:
       daway = instructions[instruction_counter]
   except:
       instruction_counter = 0
       daway = instructions[instruction_counter]

   if daway == "R":
       direction = new_coords[1]

   elif daway == "L":
       direction = new_coords[0]

   start = direction
   steps += 1
   instruction_counter += 1
   if start == "ZZZ":
       arrived = True

# Part 2
# Yeah, here goes the LCM stuff that is carefully crafted in the problem and I'd have never got to if it weren't
# for outside solutions.