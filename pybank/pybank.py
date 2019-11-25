import csv
from pathlib import Path





row_count=0
the_dates=[]
porl=[]
todatepl=0
this_to_date_p_or_l=[]
profit_change=[]
previous_row=0
this_profit_change=0
porl_change_list=[]
financial_analysis=[]

#Uses Path method of pathlib object to make paths cross platform compatible 


file_to_open = os.path.join("resources", "budget_data2.csv"

with open(file_to_open, "r") as this_csv_file:
    this_csv_reader=csv.reader(this_csv_file, delimiter=",")
    header=next(this_csv_reader)
    previous_row=0
    for row in this_csv_reader: 
           
        row_count +=1
        the_dates.append(row[0])
        #makes list of profit or loss (porl) amounts by month
        porl.append(float(row[1])) 
    
        if row_count>=2:
            porl_change=porl[row_count-1]-porl[previous_row-1]
            porl_change_list.append(porl_change)
        previous_row=row_count




        



        

total_profit_or_loss=sum(porl)


average_changes_in_porl=sum(porl_change_list)/(row_count-1)


greatest_profit_increase=(max(porl_change_list))
month_index=porl_change_list.index(max(porl_change_list))+1
greatest_profit_increase_month=the_dates[month_index]

greatest_decrease_in_porl=min(porl_change_list)
month_index=porl_change_list.index(min(porl_change_list))+1
greatest_porl_decrease_month=the_dates[month_index]

#financial_analysis is a list of each line of the results to be both printed and writen to a file
financial_analysis.append("------------------------------------------------------")
financial_analysis.append("Financial Analysis")
financial_analysis.append("------------------------------------------------------")
financial_analysis.append("Total Months: " + str(row_count))
financial_analysis.append("Total profit/loss: " + "${:,.2f}".format(total_profit_or_loss))
financial_analysis.append("Average changes in profit//loss: " +  "${:,.2f}".format(average_changes_in_porl))
financial_analysis.append("Greatest profit increase: "+  "${:,.2f}".format(greatest_profit_increase) + " in " + greatest_profit_increase_month)   
financial_analysis.append("Geatest decrease in profits: " +  "${:,.2f}".format(greatest_decrease_in_porl) + " in " + greatest_porl_decrease_month)
financial_analysis.append("------------------------------------------------------")
#Writing results to file line by line with end of line character. 
#It overwrites file if it does not exist. 

data_folder = Path("pybank/resources/")

filename = data_folder / "pybank_results.txt"
#Creates new text file in resources folder and overwrites it if it does exist.
with open(filename, "w+") as this_file:
    for i in range(0, len(financial_analysis)):
        print(financial_analysis[i])
        this_file.writelines(financial_analysis[i]+ "\n")