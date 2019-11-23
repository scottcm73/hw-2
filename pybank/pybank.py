import csv
from pathlib import Path



def to_date_profit_or_loss(the_dates, porl):
    todatesum=0
   
    todatesum=sum(porl)
    
    return todatesum

def profit_monthly_change(this_to_date_p_or_l, row_before):
    return this_to_date_p_or_l[row_before+1]-this_to_date_p_or_l[row_before]

def average_monthly_change():
    return

def total_profit_or_loss():
    return

row_count=0
the_dates=[]
porl=[]
todatepl=0
this_to_date_p_or_l=[]
profit_change=[]
previous_row=0
this_profit_change=0

#Uses Path method of pathlib object to make paths cross platform compatible 
data_folder = Path("pybank/resources/")

file_to_open = data_folder / "budget_data2.csv"

with open(file_to_open, "r") as this_csv_file:
    this_csv_reader=csv.reader(this_csv_file, delimiter=",")
    header=next(this_csv_reader)
    for row in this_csv_reader:       
        row_count +=1
        the_dates.append(row[0])
        #makes list of profit or loss (porl) amounts by month
        porl.append(int(row[1]))
        this_to_date_p_or_l.append(to_date_profit_or_loss(the_dates, porl))
        
        previous_row=row
        
       

        






    print(row_count)

    print(this_to_date_p_or_l)

   