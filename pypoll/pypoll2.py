import csv

line_count = 0
total_votes =0
counties= []
candidates=[]
vote_counter=[]
this_index=0
vote_int=0
election_results=[]
results_string=""

with open('election_data.csv', "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    header=next(csv_reader)
    print(header)
    
    for row in csv_reader:
        total_votes += 1

        if row['County'] not in counties:
            # Makes a list of only distinct counties
            counties.append(row['County'])
        

        if row['Candidate'] not in candidates:
            #Makes a list of only distinct candidates voted for
            candidates.append(row['Candidate']) 
            vote_counter.append(1)
        else:
            # Gets the integer of the vote count of the particular 
            # candidate in the candidates list with the same index as the current candidate

            candidate_index=candidates.index(row['Candidate'])
            vote_int=vote_counter[candidate_index]
            vote_int=vote_int+1
            # sets the vote_counter list at that same candidate index equal to the vote_int
            vote_counter[candidate_index]=vote_int
        
           
     
        
print("Candidates voted for include: ")
print(candidates)
print("Counties include: ")
print(counties)


#election_results is a list of each line of the results to be printed and writen to a file
election_results.append("Election Results")
election_results.append("--------------------------------------")
election_results.append("Total votes: " + str(total_votes))


print(vote_counter)

length=len(candidates)
for i in range (0, length):
    results_string=candidates[i]+ ": " + str(vote_counter[i])+ "  " + "{:.2%}".format(vote_counter[i]/total_votes)
    election_results.append(results_string)

election_results.append("--------------------------------------")  
winning_votes=max(vote_counter)
winning_index=vote_counter.index(winning_votes)
results_string="Winner: " + candidates[winning_index]
election_results.append(results_string)  
election_results.append("--------------------------------------") 
filename="results.txt"
with open(filename, "w+") as this_file:
    for i in range(0, len(election_results)):
        print(election_results[i])
        this_file.writelines(election_results[i]+ "\n")







