with open("day9.txt") as fin:
    data = fin.read().strip().split("\n")
    grid = [[int(i) for i in line] for line in data]

rows = len(grid)
cols = len(grid[0])

total_sum = 0

for row in range(rows):
    for col in range(cols):
        is_lowest = True

        # Check adjacent cells
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            adj_row = row + dx
            adj_col = col + dy

            if not (0 <= adj_row < rows and 0 <= adj_col < cols):
                continue

            if grid[adj_row][adj_col] <= grid[row][col]:
                is_lowest = False
                break

        if is_lowest:
            total_sum += grid[row][col] + 1

print("Part 1:", total_sum)


#Part 2    

def createbasin(row,col,prevval):
    for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        adj_row = row + dx
        adj_col = col + dy
        if not (0 <= adj_row < rows and 0 <= adj_col < cols):
            continue
        if (adj_row,adj_col) not in basin and grid[adj_row][adj_col] < 9 and grid[adj_row][adj_col] >= prevval:
            basin.append((adj_row,adj_col))
            createbasin(adj_row,adj_col,grid[adj_row][adj_col])

total_sum = 0
basins = []
for row in range(rows):
    for col in range(cols):
        is_lowest = True

        # Check adjacent cells
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            adj_row = row + dx
            adj_col = col + dy

            if not (0 <= adj_row < rows and 0 <= adj_col < cols):
                continue

            if grid[adj_row][adj_col] <= grid[row][col]:
                is_lowest = False
                break
        if is_lowest:
            basin = []
            createbasin(adj_row,adj_col,grid[row][col])
            basins.append(basin)

                 
basins = sorted(basins,key=len,reverse=True)

print(len(basins[0])*len(basins[1])*len(basins[2]))
