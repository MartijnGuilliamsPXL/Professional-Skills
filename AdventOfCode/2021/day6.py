import collections
#Part 1
with open("./day6.txt") as file:
    data = [int(i) for i in file.read().split(',')]
    
for i in range(80):
    for f in range(len(data)):
        if data[f] == 0:
            data[f] = 6
            data.append(8)
        else:
            data[f] = data[f] - 1

print(len(data))

#Part 2
with open("./day6.txt") as file:
    data = [int(i) for i in file.read().split(',')]

counter = collections.Counter(data)
for i in range(-1, 9):
    if i not in counter:
        counter[i] = 0

for day in range(256):
    for i in range(9):
        counter[i-1] = counter[i] #iedereen een dag minder
    counter[8] = counter[-1] #voor iedereen in -1 een nieuwe vis aanmaken
    counter[6] += counter[-1] #iedereen in -1 gaan terug naar 6
    counter[-1] = 0

total = 0
for i in range(9):
    total += counter[i]
print(total)