import os
import csv

file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

text_output = os.path.join("PyPoll", "poll_output.txt")

candidate_list = {}
linebreak = "-------------------------"

with open(file_path, encoding="utf-8") as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=",")
    poll_header = next(poll_csv)

    vote_total = 0
    for row in poll_csv:
        vote_total += 1
        candidate = row[2]
        if candidate in candidate_list:
            candidate_list[candidate] += 1
        else:
            candidate_list[candidate] = 1

    candidate_list["Pct Stockham"] = round((candidate_list["Charles Casper Stockham"]/vote_total)*100, 3)
    candidate_list["Pct DeGette"] = round((candidate_list["Diana DeGette"]/vote_total)*100, 3)
    candidate_list["Pct Doane"] = round((candidate_list["Raymon Anthony Doane"]/vote_total)*100, 3)

    winner = max(candidate_list, key=candidate_list.get)

    print("Total Votes: " + str(vote_total))
    print(linebreak)
    print("Charles Casper Stockham: " + str(candidate_list["Pct Stockham"]) + "% (" + str(candidate_list["Charles Casper Stockham"]) +")")
    print("Diana DeGette: " + str(candidate_list["Pct DeGette"]) + "% (" + str(candidate_list["Diana DeGette"]) +")")
    print("Raymon Anthony Doane: " + str(candidate_list["Pct Doane"]) + "% (" + str(candidate_list["Raymon Anthony Doane"]) +")")
    print(linebreak)
    print("Winner: " + winner)
    print(linebreak)

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