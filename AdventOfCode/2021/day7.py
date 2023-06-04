with open('day7.txt') as file:
    positions = [int(i) for i in file.read().strip().split(",")]

min_position = min(positions)
max_position = max(positions)

min_cost = float('inf')

for alignment in range(min_position, max_position + 1):
    total_cost = sum(abs(position - alignment) for position in positions)
    if total_cost < min_cost:
        min_cost = total_cost

print("part 1:", min_cost)


# Part 2

min_cost = float('inf')
max_pos = max(positions)

for pos in range(max_pos):
    req = 0
    for i in positions:
        dist = abs(i - pos)
        cost = dist * (dist + 1) // 2
        req += cost
    min_cost = min(min_cost, req)

print("part 2:",min_cost)