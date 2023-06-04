with open("day5.txt") as file:
    data = file.read().strip().split("\n")

lines = []
for line in data:
    start, _, end = line.split(" ")
    start = list(map(int, start.split(",")))
    end = list(map(int, end.split(",")))
    lines.append([start, end])

filtered_lines = []
for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    if x1 == x2 or y1 == y2:
        filtered_lines.append(line)

max_x = 0
max_y = 0
for line in filtered_lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)


cover = [[0] * (max_y + 1) for _ in range(max_x + 1)]
for line in filtered_lines:
    start, end = line
    if start[0] == end[0]:
        bottom = min(start[1], end[1])
        top = max(start[1], end[1])
        for y in range(bottom, top + 1):
            cover[start[0]][y] += 1
    else:
        left = min(start[0], end[0])
        right = max(start[0], end[0])
        y = start[1]
        for x in range(left, right + 1):
            cover[x][y] += 1

count = 0
for row in cover:
    for value in row:
        if value >= 2:
            count += 1

#print(cover)
print(count)




# Part 2

lines = []
for line in data:
    start, _, end = line.split(" ")
    start = list(map(int, start.split(",")))
    end = list(map(int, end.split(",")))
    lines.append([start, end])

filtered_lines = []
for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
        filtered_lines.append(line)

max_x = 0
max_y = 0
for line in filtered_lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)

cover = [[0] * (max_y + 1) for _ in range(max_x + 1)]
for line in filtered_lines:
    start, end = line
    if start[0] == end[0]:
        bottom = min(start[1], end[1])
        top = max(start[1], end[1])
        for y in range(bottom, top + 1):
            cover[start[0]][y] += 1
    elif start[1] == end[1]:
        left = min(start[0], end[0])
        right = max(start[0], end[0])
        for x in range(left, right + 1):
            cover[x][start[1]] += 1
    else:
        x1, y1 = start
        x2, y2 = end
        if x1 < x2:
            if y1 < y2:
                for i in range(x1, x2 + 1):
                    cover[i][y1 + i - x1] += 1
            else:
                for i in range(x1, x2 + 1):
                    cover[i][y1 - i + x1] += 1
        else:
            if y1 < y2:
                for i in range(x2, x1 + 1):
                    cover[i][y2 - i + x2] += 1
            else:
                for i in range(x2, x1 + 1):
                    cover[i][y2 + i - x2] += 1

count = 0
for row in cover:
    for value in row:
        if value >= 2:
            count += 1

print(count)


