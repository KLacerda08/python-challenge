import os
import csv

election_data = (os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv'))
with open(election_data) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #create empty lists to store information
   
    VoterID = []
    County = []
    Candidate = []
    VoteCount = []
    cand_unique = []

    #create loop to get data after header row into separate lists; populate lists; find unique candidates
    csv_header = next(csvreader)
    for row in csvreader:
        VoterID.append(int(row[0]))
        Candidate.append(row[2])
        if row[2] not in cand_unique:
            cand_unique.append(str(row[2]))

    #print(cand_unique) # - to identify candidate names

    #Count Number Votes per Candidate
    Khan_votes = Candidate.count("Khan")
    Correy_votes = Candidate.count("Correy")
    Li_votes = Candidate.count("Li")
    O_Tooley_votes = Candidate.count("O'Tooley")
    
    #Find total VoteCount and calculate percent votes for each candidate
    VoteCount = len(list(VoterID))
    Khan_percent = "{:.2%}".format(Khan_votes/VoteCount)
    Correy_percent = "{:.2%}".format(Correy_votes/VoteCount)
    Li_percent = "{:.2%}".format(Li_votes/VoteCount)
    O_Tooley_percent = "{:.2%}".format(O_Tooley_votes/VoteCount)
    
    #create list of number of votes per candidate 
    results_list = [Khan_votes, Correy_votes, Li_votes, O_Tooley_votes]
   
    #create dictionary to relate number of votes per candiate to candidate name
    results_dict = dict(zip(cand_unique, results_list)) 

    #find max value and get the winner:
    maxvalue = (max(results_list))
    winner = list(results_dict.keys())[list(results_dict.values()).index(maxvalue)]
    
#print results to terminal
    print("Election Results")
    print("--------------------------")
    print("Total Votes = " + str(VoteCount))
    print("--------------------------")
    print("Khan: " + str(Khan_percent) + " (" + str(Khan_votes) + ")")
    print("Correy: " + str(Correy_percent) + " (" + str(Correy_votes) + ")")
    print("Li: " + str(Li_percent) + " (" + str(Li_votes) +")")
    print("O'Tooley: " + str(O_Tooley_percent) + " (" + str(O_Tooley_votes) +")")
    print("--------------------------")
    print("Winner: " + str(winner))
    
#print results to textfile
with open(os.path.join('Analysis', 'Election_Results.txt'), "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("--------------------------\n")
    text_file.write("Total Votes = " + str(VoteCount) + '\n')
    text_file.write("--------------------------\n")
    text_file.write("Khan: " + str(Khan_percent) + " (" + str(Khan_votes) +")\n")
    text_file.write("Correy: " + str(Correy_percent) + " (" + str(Correy_votes) +")\n")
    text_file.write("Li: " + str(Li_percent) + " (" + str(Li_votes) +")\n")
    text_file.write("O'Tooley: " + str(O_Tooley_percent) + " (" + str(O_Tooley_votes) +")\n")
    text_file.write("--------------------------\n")
    text_file.write("Winner: " + str(winner))
    text_file.flush()
    text_file.close()
 

 