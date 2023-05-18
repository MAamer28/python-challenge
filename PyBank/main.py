#Modules are imported as needed.
import os
import csv

#The CSV file is extracted via a path defined as relative to the main "python-challenge" repository.
data_path = os.path.join("PyBank", "Resources","budget_data.csv")

#A path is created for the output text file that will be created at the end of the code.
text_output = os.path.join("PyBank", "finanalysis_output.txt")

#The variables that will be used to calculate the results are defined here.
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

#The CSV file containing the raw data is extracted and read as a dictionary, with the headers automatically read as keys.
with open(data_path, newline= '') as csvfile:
    budget_csv = csv.DictReader(csvfile)

    for row in budget_csv:
        #Firstly, the total number of months in the data file is calculated via an iterative loop by adding +1 to the total_months variable for each row of data (minus the header row) in the CSV file.
        total_months += 1

        #The net total of profits or losses is calculated via an iterative loop where each value in the 'Profit/Losses' column is added to the previous value to determine net total.
        net_total = net_total + int(row['Profit/Losses'])

        #Here, I am getting the wrong value compared to Boot Camp Spot. In calculating the rate of change, I am trying to add the sum of the values of a row and the previous row to the "rev_rate" list.
        #In other words, the below functions are meant to iterate through the column and calculate x = February - January and so on. However, the average rate of change this results in is $4448.13. 
        #The Challenge Module's page on Boot Camp Spot reflects a correct result of $-8311.11. There is something wrong here that I have been trying to fix to no avail. 
        #If these comments are still here when the assignment is corrected, it is because I ran out of time before the deadline. My aim will be to resubmit the assignment once I work on this issue further over the weekend.
        rev_change = float(row['Profit/Losses']) - prevmonth_rev
        prevmonth_rev = float(row["Profit/Losses"])
        rev_rate = [rev_change] + rev_rate
        monthly_change = [monthly_change] + [row["Date"]]

        rev_average = sum(rev_rate)/len(rev_rate)

        #Here, we determine the months each with the greatest increase in profits and greatest decrease in profits.
        if rev_change > max_gain[1]:
            max_gain[1] = rev_change
            max_gain[0] = row['Date']

        if rev_change < max_loss[1]:
            max_loss[1] = rev_change
            max_loss[0] = row['Date']
    
    
    #The results are printed to the terminal.
    print("Total Months: " + str(total_months))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(rev_average))
    print("Greatest Increase in Profits: " + str(max_gain [0]) + "($" + str(max_gain[1]) + ")")
    print("Greatest Decrease in Profits: " + str(max_loss[0]) + "($" + str(max_loss[1]) + ")") 

#The results are then written into a text file to reflect the appearance seen on the Boot Camp Spot page.
with open(text_output, "w") as file:
    file.write("Financial Analysis\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("Average Change: $" + str(rev_average) + "\n")
    file.write("Greatest Increase in Profits: " + str(max_gain [0]) + "($" + str(max_gain[1]) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(max_loss[0]) + "($" + str(max_loss[1]) + ")" + "\n")