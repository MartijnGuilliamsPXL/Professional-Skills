from string import ascii_letters
# print(ascii_letters)

with open('day3.txt') as file:
    data = [i for i in file.read().strip().split("\n")]
    
totalSum = 0
for entry in data:
    # Get the half way mark
    half = len(entry)//2
    
    # Split up the string
    leftSide = set(entry[:half])
    rightSide = set(entry[half:])

    # print(leftSide, rightSide)
    for characterl in leftSide:
        if characterl in rightSide:
            totalSum += ascii_letters.index(characterl) + 1

print("Answer to part 1: ", totalSum)



# ==== PART 2 ====
totalSum = 0
j = 3
for i in range(0, len(data), 3):
    entry = data[i:j]
    j += 3
    
    for character1 in entry[0]:
        if character1 in entry[1] and character1 in entry[2]:
            totalSum += (ascii_letters.index(character1) + 1) 
            break
     
print("Answer to part 2: ", totalSum)

