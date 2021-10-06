#Import libraries
import pathlib

import csv
from statistics import mean, median, mode


#Read in the data
csv = pathlib.Path("Resources", "budget_data.csv")

#Empty lists to populate
months = []
profit_losses = []

PL_change = []

#Read CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        months.append(row[0])
        profit_loses.append(int(row[1]))

        
#Calculate the total number of months
total_months = len(months)

#Calc the total net profit/loss
total_months = len(months)
total_amount = sum(profit_losses)

PL_tosubtract =  zip(profit_losses[0:], profit_losses[1:])
#changes in P&L for each month
PL_change = [(j-i) for i,j in PL_tosubtract]

#Calc the avg change in P&L
Average = mean(PL_change)

#Converted list to dictionary to use in analysis
months_PLchg = dict(zip(months[1:], PL_change))

#Calc  min and max in P&L
lowest_profit = min(months_PLchg.keys(), key=(lambda k: months_PLchg[k]))
highest_profit = max(months_PLchg.keys(), key=(lambda k: months_PLchg[k]))


#Summary
#Export script text to file with the results
budget_summary = pathlib.Path('PyBank_output = pathlib.Path("Analysis/PyBank_Analysis.txt")')

#Formatting summary table for number of months, total funds, average change, greatest profit, and least profit in terminaal and text file
with open(budget_summary,'w') as resultsfile:
        csvwriter = csv.writer(resultsfile)
        budget_summary = (
        f"\n\nFinancial Analysis\n"
        f"-----------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${format(total_funds,',d')}\n"
        f"Average Change: ${average} \n"
        f"Greatest Increase in Profits: {greatestprofit_monthyear} (${format(greatest_profit,',d')})\n"
        f"Greatest Decrease in Profits: {greatestloss_monthyear} (${format(greatest_loss,',d')})\n")
        print(budget_summary)
        resultsfile.write(budget_summary)


#Summary
print("Financial Analysis")
print("-------------------")
print(f'Total Months: {total_months}') 
print(f"Total Net Profit/Losses:  ${total_amount}") 
print(f"Average Change in Profit/Losses: ${Average:.2f}")  
print(f"Greatest Increase in Profits: {highest_profit}, ({months_PLchg[highest_profit]})")
print(f"Greatest Decrease in Profits: {lowest_profit}, ({months_PLchg[lowest_profit]})")

# Establish the file and path 
PyBank_output = pathlib.Path("Analysis/PyBank_Analysis.csv")

with open(file=PyBank_output, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total Net P&L', 'Average Change in P&L', 'Month/Yr with Greatest Increase in Profit', 'Amount of Greatest Increase',
    'Month/Yr with Greatest Decrease in Profit', 'Amount of Greatest Decrease'])

    csvwriter.writerow([total_months, total_amount, Average, highest_profit, months_PLchg[highest_profit], lowest_profit, months_PLchg[lowest_profit]])
