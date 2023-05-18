import os
import csv

data_path = os.path.join("Resources", "budget_data.csv")

money = 0

with open(data_path, "r") as csvfile:
    budget_csv = csv.reader(csvfile)

    row_count = sum(1 for row in budget_csv)
    print(row_count)

