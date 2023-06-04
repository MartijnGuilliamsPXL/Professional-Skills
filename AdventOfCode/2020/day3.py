with open('day3.txt', 'r') as file:
    data = file.read().splitlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1

for slope in slopes:
    right = slope[0]
    down = slope[1]
    row = 0
    col = 0
    count = 0

    while row < len(data):
        if data[row][col] == '#':
            count += 1
        col = (col + right) % len(data[0])
        row += down
    print(count)
    product = count * product

print(product)
