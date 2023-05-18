import os
import csv

data_path = os.path.join("PyBank", "Resources","budget_data.csv")

text_output = ("output.txt")

total_months = 0
net_total = 0
monthly_rev = []
prevmonth_rev = 0
monthly_change = []
rev_change = 0
max_loss = ["", 999999999]
max_gain = ["", 0]
rev_rate = []
rev_average = 0

with open(data_path, newline= '') as csvfile:
    budget_csv = csv.DictReader(csvfile)

    for row in budget_csv:

        total_months += 1

        net_total = net_total + int(row['Profit/Losses'])

        rev_change = float(row['Profit/Losses']) - prevmonth_rev
        prevmonth_rev = float(row["Profit/Losses"])
        rev_rate = rev_rate + [rev_change]
        monthly_change = [monthly_change] + [row["Date"]]

        if rev_change > max_gain[1]:
            max_gain[1] = rev_change
            max_gain[0] = row['Date']

        if rev_change < max_loss[1]:
            max_loss[1] = rev_change
            max_loss[0] = row['Date']
    
    rev_average = sum(rev_rate)/len(rev_rate)

with open(text_output, "w") as file:
    file.write("Financial Analysis\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % net_total)
    file.write("Average Change $%d\n" %rev_average)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (max_gain[0], max_gain[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (max_loss[0], max_loss[1]))
