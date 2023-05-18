import os
import csv

data_path = os.path.join("PyBank", "Resources","budget_data.csv")

net_total = 0

with open(data_path, newline= '') as csvfile:
    budget_csv = csv.DictReader(csvfile)

    for row in budget_csv:
        print(dict(row))
        net_total = net_total + int(row['Profit/Losses'])

print(net_total)