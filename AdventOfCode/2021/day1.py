with open('day1.txt') as file:
    data = [int(i) for i in file.read().strip().split("\n")]
#print(data)

count = 0 

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        count += 1

print(count)





# Part 2
count = 0

moving_sum = sum(data[:3])
prev_moving_sum = moving_sum + 1 # start met een grotere prev

for i in range(len(data) - 3):
    if moving_sum > prev_moving_sum:
        count += 1

    prev_moving_sum = moving_sum

    # Update moving sum
    moving_sum -= data[i]
    moving_sum += data[i + 3]

if moving_sum > prev_moving_sum:
    count += 1

print(count)