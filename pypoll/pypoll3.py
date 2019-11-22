#Python 3.7 object

vote_tally=0
vote_tally_by_county=0
counties=[]
total_votes=0
candidates=[]
class Vote:
    total_votes=total_votes+1

    def _init_(self, voter_id, county, vote_for_candidate):
        self.voter_id=voter_id
        self.county=county
        self.vote_for_candidate=vote_for_candidate
    
    def candidate_list(self, this_candidate, candidates):
        if this_candidate not in candidates:
            # Makes a list of only distinct counties
            candidates.append(this_candidate)
        return

    def county_list(self, this_county, counties):
        if this_county not in counties:
            # Makes a list of only distinct counties
            counties.append(this_county)
        return

    def running_vote_tally_by_candidate(self):
        

        return vote_tally
    
    def running_tally_by_candidate_and_county(self):
        
        return vote_tally_by_county


   
    

    



    
    


    
