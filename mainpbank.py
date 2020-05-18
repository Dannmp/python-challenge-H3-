#Py bank importar archivo budget

import os
import csv

print("Financial Analysis")
print("-------------------------------------------")

csvpath = os.path.join("budget_data.csv")

profits = 0
var_prof_list = []
prev_prof = 0
month_of_change = [0]
total_prof = 0
months = []

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    header = next(reader)

    for row in reader:

        profits = int(row[1]) - prev_prof
        prev_prof = int(row[1])
        var_prof_list += [profits]
        month_of_change += [row[0]]
        total_prof += int(row[1])
        months += [row[0]]

tmonths = len(month_of_change) -1
increase = max(var_prof_list)
decrease = min(var_prof_list)

month_increase = var_prof_list.index(max(var_prof_list))
month_decrease = var_prof_list.index(min(var_prof_list))

print(f'{str("Total Months:")} {tmonths}')
print (f'{str("Total: $")}{total_prof}')
print(f'{str("Average Change")} {round(sum(var_prof_list[1:])/len(var_prof_list[1:]),2)}')
print(f"Greatest Increase in Profits: {months[month_increase]} (${(str(increase))})")
print(f'{str("Greatest Decrease in Profits:")} {months[month_decrease]} {"("}{"$"}{decrease}{")"}')
