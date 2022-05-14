

def read_input():
    with open('Day2.txt') as f:
        raw_lines = f.readlines()
    return raw_lines


directions = []

for i in read_input():
    directions.append(i.strip('\n'))

horizontal = 0
depth = 0

for direction in directions:
    direction_split = direction.split(" ")
    command = direction_split[0]
    int_direction = int(direction_split[1])
    if command == "forward":
        horizontal += int_direction
    elif command == "down":
        depth += int_direction
    elif command == "up":
        depth -= int_direction

print(depth * horizontal)
