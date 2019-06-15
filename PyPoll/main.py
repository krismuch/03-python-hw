#import modules
import os
import csv

#point to csv file
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #ignore header
    csv_header = next(csvreader)

    #initialize variables
    total_votes=0
    vote_list=[]
    unique_canidate_list=[]
    khan_votes=0
    correy_votes=0
    li_votes=0
    otooley_votes=0

    #determine number total votes, grab canidate column
    for row in csvreader:
        total_votes += 1
        vote_list.append(row[2])

    #get list of unique canidates
    for x in vote_list: 
        # check if exists in unique_list or not 
        if x not in unique_canidate_list: 
            unique_canidate_list.append(x) 

    #get total votes for each canidate
    for i in range(1,len(vote_list)):
        if vote_list[i] == "Khan":
            khan_votes += 1
        if vote_list[i] == "Correy":
            correy_votes += 1
        if vote_list[i] == "Li":
            li_votes += 1
        if vote_list[i] == "O'Tooley":
            otooley_votes += 1

#figure out the maxmimum vote to help determine winner
maxvotes = max(khan_votes,correy_votes,li_votes,otooley_votes)

#determining winner
def winner():
    if maxvotes == khan_votes:
        return "Khan"
    if maxvotes == correy_votes:
        print("Correy")
    if maxvotes == li_votes:
        print("Li")
    if maxvotes == otooley_votes:
        print("O'Tooley")

#store winner in variable to print
winnername=winner()
         
#print to terminal
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})")
print(f"Correy: {round((correy_votes/total_votes)*100,3)}% ({correy_votes})")
print(f"Li: {round((li_votes/total_votes)*100,3)}% ({li_votes})")
print(f"O'Tooley: {round((otooley_votes/total_votes)*100,3)}% ({otooley_votes})")
print("-----------------------------")
print(f"Winner: {winnername}")
print("-----------------------------")

#print to csv
# Specify the file to write to
output_path = os.path.join("Output", "pybank_winner.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write to file
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f"Khan: {round((khan_votes/total_votes)*100,3)}% ({khan_votes})"])
    csvwriter.writerow([f"Correy: {round((correy_votes/total_votes)*100,3)}% ({correy_votes})"])
    csvwriter.writerow([f"Li: {round((li_votes/total_votes)*100,3)}% ({li_votes})"])
    csvwriter.writerow([f"O'Tooley: {round((otooley_votes/total_votes)*100,3)}% ({otooley_votes})"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow([f"Winner: {winnername}"])
    csvwriter.writerow(["-----------------------------"])