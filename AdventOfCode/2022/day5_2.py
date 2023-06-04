from string import ascii_uppercase

# Getting input
with open('day5.txt') as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))
    
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]


for string in stack_strings[:-1]:
    stack_num = 1
    for index in indexes:
        if string[index] == " ":
            pass
        else:
            stacks[stack_num].insert(0, string[index])
        stack_num += 1

print("\n\nStacks:\n")
for stack in stacks:
    print(stack, stacks[stack])
print("\n")


for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    instruction[0]
    instruction[1]
    instruction[2]
    
    letters = stacks[instruction[1]][-instruction[0]:]
    del stacks[instruction[1]][-instruction[0]:]
    #print(letters)
    stacks[instruction[2]].extend(letters)

for stack in stacks:
    print(stack, stacks[stack])
print("\n")



