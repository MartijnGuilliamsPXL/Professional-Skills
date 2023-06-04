with open("day1.txt") as file:
    data = file.read().strip().split("\n")

calorie_sum = 0
max_calories = 0

for line in data:
    if line.strip():
        calorie_sum += int(line)
    else:
        max_calories = max(max_calories, calorie_sum)
        calorie_sum = 0

print("Part 1:", max_calories)


# Part 2

calorie_sum = 0
top_calories = [0, 0, 0]

for line in data:
    if line.strip():
        calorie_sum += int(line)
    else:
        top_calories.sort(reverse=True)
        top_calories[2] = max(top_calories[2], calorie_sum)
        calorie_sum = 0

total_calories = sum(top_calories)
print("Part 2:", total_calories)