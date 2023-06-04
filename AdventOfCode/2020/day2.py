# Read the password list from a file
with open('day2.txt', 'r') as file:
    password_list = file.read().splitlines()

count = 0
passwords1 = password_list.copy()
for entry in passwords1:
    policy, passwords1 = entry.split(": ")
    limits, letter = policy.split()
    min_limit, max_limit = map(int, limits.split("-"))

    occurrences = passwords1.count(letter)

    if min_limit <= occurrences <= max_limit:
        count += 1

print(count)



#Part 2

count = 0
passwords2 = password_list.copy()
for entry in passwords2:
    policy, passwords2 = entry.split(": ")
    positions, letter = policy.split()
    pos1, pos2 = map(int, positions.split("-"))

    if (passwords2[pos1-1] == letter) != (passwords2[pos2-1] == letter):
        count += 1

valid_passwords = count

print(valid_passwords)
