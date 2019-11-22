#Python 3.7 object

vote_tally=0
vote_tally_by_county=0
counties=[]
total_votes=0
candidates=[""]
class Vote:
    total_votes=total_votes+1


    def _init_(self, voter_id, county, vote_for_candidate):
        self.voter_id=voter_id
        self.county=county
        self.vote_for_candidate=vote_for_candidate
    
    def running_vote_tally_by_candidate(self, candidates, vote_tally):
        # Gets the integer of the vote count of the particular 
        # candidate in the candidates list with the same index as the current candidate
        for i in range(len(candidates)):
            candidate_index=i
            vote_int=vote_tally[candidate_index]
            vote_int=vote_int+1
            # sets the vote_counter list at that same candidate index equal to the vote_int
            vote_tally[candidate_index]=vote_int

        return vote_tally

    def running_tally_by_candidate_and_county(self, candidates, vote_tally_by_county):
        return vote_tally_by_county

    
    
    def candidate_list(self, this_candidate, candidates):
        if this_candidate not in candidates:
            # Makes a list of only distinct counties
            candidates.append(this_candidate)
        
        else: 
            self.running_vote_tally_by_candidate(candidates, vote_tally)
        return candidates
    
    

    def county_list(self, this_county, counties):
        if this_county not in counties:
            # Makes a list of only distinct counties
            counties.append(this_county)
        return counties

    
    


   
    

    



    
    


    
