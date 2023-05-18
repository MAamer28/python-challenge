#First, we import the modules we will use.
import os
import csv

#The file path is defined relative to the main "python-challenge" repository.
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

#We also define the path for the text file that will be created at the end of the assignment.
text_output = os.path.join("PyPoll", "poll_output.txt")

#We define some variables, namely the candidate list to be a dictionary and a "line-break" variable that we will use to create the breaks to clean up the presentation of the data at the end.
candidate_list = {}
linebreak = "-------------------------"

#The CSV file is read by Python and the headers are fixed.
with open(file_path, encoding="utf-8") as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=",")
    poll_header = next(poll_csv)

    #We calculate the total number of votes in the poll. Firstly, we set the vote total as 0.
    #Then, we create an iterative loop where every row adds +1 to the vote total.
    #Candidates are defined as being in the column corresponding to index = 2. 
    #Each candidate receives +1 vote for every row in which their name is listed in the "Candidates" column, i.e. Index = 2 Column.
    vote_total = 0
    for row in poll_csv:
        vote_total += 1
        candidate = row[2]
        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate] = 1

    #The percentage of votes for each candidate are calculated as the number of votes for a given candidate divided by the total number of votes, multiplied by 100.
    #Note that the parameter "3" here in the "round" function indicates each % value will be rounded to 3 decimal places.
    candidate_list["Pct Stockham"] = round((candidate_list["Charles Casper Stockham"]/vote_total)*100, 3)
    candidate_list["Pct DeGette"] = round((candidate_list["Diana DeGette"]/vote_total)*100, 3)
    candidate_list["Pct Doane"] = round((candidate_list["Raymon Anthony Doane"]/vote_total)*100, 3)

    #The winner is determined as the candidate with the highest number of votes, or the maximum nunber in the list aggregating the number of votes of each candidate.
    winner = max(candidate_list, key=candidate_list.get)

    #The results are printed and tabulated as follows.
    print("Total Votes: " + str(vote_total))
    print(linebreak)
    print("Charles Casper Stockham: " + str(candidate_list["Pct Stockham"]) + "% (" + str(candidate_list["Charles Casper Stockham"]) +")")
    print("Diana DeGette: " + str(candidate_list["Pct DeGette"]) + "% (" + str(candidate_list["Diana DeGette"]) +")")
    print("Raymon Anthony Doane: " + str(candidate_list["Pct Doane"]) + "% (" + str(candidate_list["Raymon Anthony Doane"]) +")")
    print(linebreak)
    print("Winner: " + winner)
    print(linebreak)

#The output is then aggregated into a text file as follows, with the text file created in the path defined above.
with open(text_output, "w") as file:
    file.write("Election Results" + "\n")
    file.write(linebreak + "\n")
    file.write("Total Votes: " + str(vote_total) + "\n")
    file.write(linebreak + "\n")
    file.write("Charles Casper Stockham: " + str(candidate_list["Pct Stockham"]) + "% (" + str(candidate_list["Charles Casper Stockham"]) +")" + "\n")
    file.write("Diana DeGette: " + str(candidate_list["Pct DeGette"]) + "% (" + str(candidate_list["Diana DeGette"]) +")" + "\n")
    file.write("Raymon Anthony Doane: " + str(candidate_list["Pct Doane"]) + "% (" + str(candidate_list["Raymon Anthony Doane"]) +")" + "\n")
    file.write(linebreak + "\n")
    file.write("Winner: " + winner + "\n")
    file.write(linebreak + "\n")