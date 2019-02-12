import os 
import csv

csvpath = os.path.join('..', "PyPoll", "election_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # create variable for calculations
    vote_count = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    winner = ''
    winner_votes = 0

    # Read each row of data after the header
    for row in csvreader:

        # count the  total votes 
        vote_count += 1

        # calculate the vote for each candidate
        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1

    # Calculate the winner
        if Khan_votes > winner_votes:
            winner = "Khan"
            winner_votes = Khan_votes
        elif Correy_votes > winner_votes:
            winner = "Correy"
            winner_votes = Correy_votes
        elif Li_votes > winner_votes:
            winner = "Li"
            winner_votes = Li_votes
        elif OTooley_votes > winner_votes:
            winner = "O'Tooley"
            winner_votes = OTooley_votes


    # calculate the percentage of the vote for each candidate
    Khan_percent = (Khan_votes / vote_count) * 100
    Khan_percent = round(Khan_percent, 3)
    Khan_percent = float(Khan_percent)

    Correy_percent = (Correy_votes / vote_count) * 100
    Correy_percent = round(Correy_percent, 3)
    Correy_percent = float(Correy_percent)

    Li_percent = (Li_votes / vote_count) * 100
    Li_percent = round(Li_percent, 3)
    Li_percent = float(Li_percent)

    OTooley_percent = (OTooley_votes / vote_count) * 100
    OTooley_percent = round(OTooley_percent, 3)
    OTooley_percent = float(OTooley_percent)

    # print results
    print("Election Results")
    print("--------------------------")    
    print("Total Votes:" , vote_count)
    print("--------------------------")
    print("Khan:", Khan_percent,"% ", Khan_votes) 
    print("Correy:", Correy_percent,"% ", Correy_votes)
    print("Li:", Li_percent,"% ", Li_votes)
    print("O'Tooley:",OTooley_percent,"% ", OTooley_votes)
    print("--------------------------")
    print("Winner:", winner)
    print("--------------------------")