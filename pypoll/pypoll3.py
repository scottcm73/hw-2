#Python 3.7 object
import csv

#global scope




class vote:
    

    def _init_(self):
        return
    
    def running_vote_tally_by_candidate(self):
        # Gets the integer of the vote count of the particular 
        # candidate in the candidates list with the same index as the current candidate
        



        return

    def running_tally_by_candidate_and_county(self):
      

        return 

    
    
    def candidate_list(self):
        
        return 
    
    

    def county_list(self):
        
        return



  
    
with open('election_data.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header=next(csv_reader)
    for row in csv_reader:
        this_candidate=row[2]
        this_voter_id=row[0]
        this_county=row[1]
        vote(this_voter_id, this_candidate, this_county)


   
    

    



    
    


    
