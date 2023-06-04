with open("./day3.txt") as file:
    data = file.read().strip().split("\n")

gammaBinGetal = ""
epsilonBinGetal = ""

num_columns = len(data[0])


for col_index in range(num_columns):
    enen = 0
    nullen = 0
    for row in data:
        element = row[col_index]
        # Perform operations on each element
        if element == '1':
            enen += 1
        else:
            nullen += 1
        #print(enen, nullen)
    
    if enen > nullen:
        gammaBinGetal += "1"
        epsilonBinGetal += "0"
    else:
        gammaBinGetal += "0"
        epsilonBinGetal += "1"

gammaGetal = int(gammaBinGetal, 2)
epsilonGetal = int(epsilonBinGetal, 2)
print(gammaGetal * epsilonGetal)


# Part 2

N = len(data[0])


# oxygen
lst = data.copy()
for i in range(N):
    if len(lst) <= 1:
        break
    
    count0 = sum(1 for x in lst if x[i] == '0')
    count1 = len(lst) - count0
    v = '0' if count0 > count1 else '1'
    lst = [x for x in lst if x[i] == v]

oxygen = int(lst[0], 2)
#print("oxygen", oxygen)


# CO2
lst = data.copy()
for i in range(N):
    if len(lst) <= 1:
        break
    
    count0 = sum(1 for x in lst if x[i] == '0')
    count1 = len(lst) - count0
    v = '0' if count0 <= count1 else '1'
    
    lst = [x for x in lst if x[i] == v]
    
    
    

co2 = int(lst[0], 2)
#print("co2", co2)

# life support
print(co2 * oxygen)