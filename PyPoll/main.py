
import os
import csv

csvpath = os.path.join("/Users/gibranahmad/python_challenge/PyPoll/election_data.csv")
file_output = "poll_results.txt"
 
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""


with open(csvpath, newline = "") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter = ",", )
    next(csvreader, None)
    for row in csvreader:
        
        total_votes += 1
        
        if row['Candidate'] in candidates.keys():
            candidates[row['Candidate']] += 1
        else:
            candidates[row['Candidate']] = 1

        
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

         
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    if (str(candidates_percent[key]) != None)  and key != None and str(value) != None:
        print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")


with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        if (str(candidates_percent[key]) != None)  and key != None and str(value) != None:
            file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")