# Getting data
with open('day4.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


# === PART 1 ===
overlapped_pairs = 0
for entry in data:
    first_pair, second_pair = entry.split(",")
    first_pair = [int(i) for i in first_pair.split("-")]
    second_pair = [int(i) for i in second_pair.split("-")]

    if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]:
        overlapped_pairs += 1
    elif second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]:
        overlapped_pairs += 1

print("Answer to part 1:", overlapped_pairs)

# === PART 2 ===
overlapping_amount_pairs = 0
for entry in data:
    first_pair, second_pair = entry.split(",")
    first_pair = [int(i) for i in first_pair.split("-")]
    second_pair = [int(i) for i in second_pair.split("-")]

    if (first_pair[0] >= second_pair[0] and first_pair[0] <= second_pair[1]) or (first_pair[1] >= second_pair[1] and first_pair[1] <= second_pair[1]):
        overlapping_amount_pairs += 1
    elif (second_pair[0] >= first_pair[0] and second_pair[0] <= first_pair[1]) or (second_pair[1] >= first_pair[1] and second_pair[1] <= first_pair[1]):
        overlapping_amount_pairs += 1

print("Answer to part 2:", overlapping_amount_pairs)