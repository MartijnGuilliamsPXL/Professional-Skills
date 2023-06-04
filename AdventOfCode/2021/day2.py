with open("./day2.txt") as file:
    data = file.read().strip().split("\n")
#print(data[0])

position = 0
depth = 0
#print(data[5][3])

for line in range(len(data)):
    if "forward" in data[line]:
        position += int(data[line][8])
    elif "up" in data[line]:
        depth -= int(data[line][3])
    elif "down" in data[line]:
        depth += int(data[line][5])


print("Part 1: ", position * depth)



# Part 2
position = 0
depth = 0
aim = 0


for line in range(len(data)):
    if "forward" in data[line]:
        position += int(data[line][8])
        depth += aim * int(data[line][8])
    elif "up" in data[line]:
        #depth -= int(data[line][3])
        aim -= int(data[line][3])
    elif "down" in data[line]:
        #depth += int(data[line][5])
        aim += int(data[line][5])


print("Part 2: ", position * depth)
