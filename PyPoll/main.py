import os
import csv

#develop code on test file named election_test

election_test = (os.path.join(os.path.dirname(__file__), 'Resources', 'election_test.csv'))
with open(election_test) as csvfile:
    
    # define csvreader. csvreader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #create empty lists to store information
   
    VoterID = []
    County = []
    Candidate = []
    VoteCount = []
    cand_unique = []

    #go to first row of data after the header
    csv_header = next(csvreader)
    
    #create loop to get data after header row into separate lists
    for row in csvreader:

        #populate VoterID list as integer
        VoterID.append(int(row[0]))
        #populate county and Candidate list as strings
        #County.append(row[2])
        Candidate.append(row[2])

        #get unique list of candidates        
        if row[2] not in cand_unique:
            cand_unique.append(str(row[2]))
       
    #Print Lists to confirm
    #print(str(cand_unique))
    #print(VoterID)

    #Find number of total votes
    VoteCount = len(list(VoterID))
    #print(VoteCount)

    #Count Number Votes per Candidate - there must be way to automatically call these names from the list rather
    #than print them and then hard code them here
    Khan_votes = Candidate.count("Khan")
    Correy_votes = Candidate.count("Correy")
    Li_votes = Candidate.count("Li")
    O_Tooley_votes = Candidate.count("O'Tooley")
    
    #test that this works
    #print(Khan_votes)
    #print(Correy_votes)
    #print(Li_votes)
    #print(O_Tooley_votes)

    #Calculate percent votes for each candidate

    Khan_percent = "{:.2%}".format(Khan_votes/VoteCount)
    Correy_percent = "{:.2%}".format(Correy_votes/VoteCount)
    Li_percent = "{:.2%}".format(Li_votes/VoteCount)
    O_Tooley_percent = "{:.2%}".format(O_Tooley_votes/VoteCount)
    
    #test that this works
    #print(Khan_percent)
    #print(Correy_percent)
    #print(Li_percent)
    #print(O_Tooley_percent)

    results_list = [Khan_votes, Correy_votes, Li_votes, O_Tooley_votes]
    
    #find max and min values of change for integers:
    maxvalue = (max([i for i in results_list if isinstance(i, int)]))
    
    #create dictionary
    results_dict = dict(zip(cand_unique, results_list)) 

    #find max value and get the winner:
    winner = list(results_dict.keys())[list(results_dict.values()).index(maxvalue)]
    #print(winner)


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
 
       

        