import csv
from pathlib import Path



def to_date_profit_or_loss(the_dates, porl):
    todatesum=0
   
    todatesum=sum(porl)
    
    return todatesum

def profit_monthly_change():
    return

def average_monthly_change():
    return

def total_profit_or_loss():
    return


data_folder = Path("pybank/resources/")

file_to_open = data_folder / "budget_data2.csv"

with open(file_to_open, "r") as this_csv_file:
    this_csv_reader=csv.reader(this_csv_file)
    row_count=0
    the_dates=[]
    porl=[]
    todatepl=0
    this_to_date_p_or_l=[]
    header=next(this_csv_reader)
    previous_row=0
    for row in this_csv_reader:       
        row_count +=1
        the_dates.append(row[0])
        porl.append(float(row[1]))
        todatepl=to_date_profit_or_loss(the_dates, porl)
        previous_row=row
       

        






    print(row_count)

    print(this_to_date_p_or_l)