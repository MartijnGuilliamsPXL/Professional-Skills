with open('day1.txt', 'r') as file:
    expense_report = [int(line.strip()) for line in file]
    
for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            if expense_report[i] + expense_report[j] == 2020:
                product = expense_report[i] * expense_report[j]
print(product)


#Part 2

for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            for k in range(j + 1, len(expense_report)):
                if expense_report[i] + expense_report[j] + expense_report[k] == 2020:
                    product = expense_report[i] * expense_report[j] * expense_report[k]
print(product)
