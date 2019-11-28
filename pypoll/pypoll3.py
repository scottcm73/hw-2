import csv


total_votes =0
counties= []
candidates=[]
vote_counter=[]
vote_num=0
election_results=[]
results_string=""
vote_counter_dict={}







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
            #Makes a list of any number of only distinct candidates voted for
            #and appends to the list each time a candidate receives a vote for the
            #first time. 
            candidates.append(row['Candidate']) 
            #gives a candidate their first vote
            vote_counter_dict[row['Candidate']]=1
        else:
            # This assumes that someone has voted for ths candidate before. 
            # It changes the value, vote_num in vote_counter_dict associated 
            # with the candidate with a certain name. 

            vote_num=vote_counter_dict[row['Candidate']]
            vote_num=vote_num+1
            #Value of vote_num for that candidate is changed in vote_counter_dict 
            #to reflect one additional vote.
            vote_counter_dict[row['Candidate']]=vote_num
            
        
           
#printing before making results into list 
   
print(vote_num)      
print("Candidates voted for include: ")
print(candidates)
print("Counties include: ")
print(counties)


#election_results is a list of each line of the results to be both printed and writen to a file
election_results.append("Election Results")
election_results.append("--------------------------------------")
election_results.append("Total votes: " + str(total_votes))

length=len(candidates)

#Finds the key value pair with the highest value which reflects the number of votes 
#for a particular candidate.
winner=max(vote_counter_dict, key=vote_counter_dict.get) 
print(winner)
   
  


# Puts results into strings with percentage formated for future 
# printing and writing to a file.

for k, v in vote_counter_dict.items():
    percentage=100* v/total_votes
    results_string=k + ": %4.2f%%" %percentage + "  " + str(v)
    election_results.append(results_string)


results_string=winner + " wins!"

election_results.append("--------------------------------------")  


election_results.append(results_string)  
election_results.append("--------------------------------------") 
filename="results.txt"

#Writing results to file line by line with end of line character. 
#It creates a file if it does not exist or overwrites it if it does.
with open(filename, "w+") as this_file:
    for i in range(0, len(election_results)):
        print(election_results[i])
        this_file.writelines(election_results[i]+ "\n")










