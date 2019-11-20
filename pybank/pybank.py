import csv
from pathlib import Path



def to_date_profit_or_loss(porl_month, porl_ammount ):
    return

def profit_monthly_change():
    return

def average_monthly_change():
    return

def total_profit_or_loss():
    return


data_folder = Path("pybank/resources/")

file_to_open = data_folder / "budget_data2.csv"

with open(file_to_open, "r") as this_csv_file:
    this_csv_reader=csv.DictReader(this_csv_file)
    row_count=0
    for row in this_csv_reader:
        print (row.keys())
        row_count +=1
        row['Date'], row['Profit/Loss']




    print(row_count)