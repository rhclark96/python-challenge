#import useful modules
import os
import csv

#set path to csv
poll_path = os.path.join("c:/Users/Rowan/Desktop/Data_Analysis_Projects/M3_Finances_Voting_Analysis_PYTHON/python-challenge/PyPoll/Resources/election_data.csv")

#set initial variable to count votes
total_votes = 0

#create list of candidates
candidate_list = []

#set initial value for previous row
prev_row=0

#create variable to hold vote counts for each candidate
stockham_count = 0
degette_count = 0
doane_count = 0

#read file
with open(poll_path, encoding='UTF-8') as poll_file:
    pollread = csv.reader(poll_file, delimiter=",")

    #skip header
    poll_header = next(pollread)

    for row in pollread:
        #add total number of votes
        total_votes += 1
        #print value to check functionality, comment out
        #print(total_votes)

        #create list of candidates, unique values only 
        if row[2] not in candidate_list:
            candidate_list.append(str(row[2]))
            #print value to check functionality, comment out
            #print(candidate_list)

            #count number of votes for Charles Casper Stockham
        if row[2] == "Charles Casper Stockham":
            stockham_count += 1
          

            #count number of votes for Diana DeGette
        if row[2] == "Diana DeGette":
            degette_count += 1

            #count number of votes for Raymon Anthony Doane
        if row[2] == "Raymon Anthony Doane":
            doane_count += 1
#print candidate counts to check functionality, comment out later
#print(stockham_count)
#print(degette_count)
#print(doane_count)

#calaulate percentages
stockham_percent = (stockham_count/total_votes).__format__(".3%")
degette_percent = (degette_count/total_votes).__format__(".3%")
doane_percent = (doane_count/total_votes).__format__(".3%")
#print to check functionality, comment out later
#print(stockham_percent)
#print(degette_percent)
#print(doane_percent)

#print all values in desired format
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate_list[0]}: {stockham_percent} ({stockham_count})")
print(f"{candidate_list[1]}: {degette_percent} ({degette_count})")
print(f"{candidate_list[2]}: {doane_percent} ({doane_count})")
print("-------------------------")
print(f"Winner: {candidate_list[1]}")

#print as .txt file 
with open("PyPoll_Analysis.txt", "a") as f:
    print("Election Results", file=f)
    print("-------------------------",file=f)
    print(f"Total Votes: {total_votes}",file=f)
    print("-------------------------",file=f)
    print(f"{candidate_list[0]}: {stockham_percent} ({stockham_count})", file=f)
    print(f"{candidate_list[1]}: {degette_percent} ({degette_count})", file=f)
    print(f"{candidate_list[2]}: {doane_percent} ({doane_count})", file=f)
    print("-------------------------", file=f)
    print(f"Winner: {candidate_list[1]}", file=f)
