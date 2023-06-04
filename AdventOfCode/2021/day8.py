with open("./day8.txt") as file:    
    data = file.read().splitlines()
data = [x.split('|') for x in data]
data = [(i.split(), o.split()) for i, o in data]

count1 = 0
count4 = 0
count7 = 0
count8 = 0
for d in data:
    for p in d[1]:
        if(len(p) == 2):
            count1 += 1
        elif(len(p) == 4):
            count4 += 1
        elif(len(p) == 3):
            count7 += 1
        elif(len(p) == 7):
            count8 += 1
print(count1+count4+count7+count8)


#part2

total = 0
for d in data:

    # Find wires representations of 1, 4, 7, 8 based on number of wires used
    for p in d[0]:
        p = ''.join(sorted(p))
        if(len(p) == 2):
            one = p
        elif(len(p) == 4):
            four = p
        elif(len(p) == 3):
            seven = p
        elif(len(p) == 7):
            eight = p

    # Deduce others digits only by comparing wires with representation of 1, 4, 7, 8
    for p in d[0]:
        p = ''.join(sorted(p))

        # 0, 6 and 9 have 6 segments
        if len(p) == 6:
            if len(set(p).intersection(four)) == 4:
                nine = p
            elif len(set(p).intersection(one)) == 2:
                zero = p
            else:
                six = p

        # 2, 3 and 5 have 5 segments
        if len(p) == 5:
            if len(set(p).intersection(one)) == 2:
                three = p
            elif len(set(p).intersection(four)) == 2:
                two = p
            else:
                five = p

    match = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }
    
    value = ""
    for x in d[1]:
        value += match[''.join(sorted(x))]
    total += int(value)

print(total)