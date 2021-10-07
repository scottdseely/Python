#import libraries
import pathlib
import csv
from statistics import mean

#Set path to budget_data
csvpath = pathlib.Path("Resources", "budget_data.csv")

#Empty lists 
months = []
profit_losses = []
PL_change = []

#Read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
     # Read the header row - skip for datasets without header 
    csvheader = next(csvreader)

     # Read each row 
    for row in csvreader:
        
        months.append(row[0])
        profit_losses.append(int(row[1]))

#Total months
total_months = len(months)

#Total P/L
total_amount = sum(profit_losses)

#Set corresponding elements that will be aggregated to produce P&L change 
PL_tosubtract =  zip(profit_losses[0:], profit_losses[1:])

#List comprehension that will produce the changes in P&L for each month
PL_change = [(j-i) for i,j in PL_tosubtract]

#Average change in P/L
Average = mean(PL_change)

#Convert list to dictionary to use in the summary
#Used months (starting at index 1) as key and the corresponding change in P/L as the value
months_PLchg = dict(zip(months[1:], PL_change))

#Calculates greatest increase/decrease in P/L
highest_profit = max(months_PLchg.keys(), key=(lambda k: months_PLchg[k]))
lowest_profit = min(months_PLchg.keys(), key=(lambda k: months_PLchg[k]))

#Summary
print("Financial Analysis")
print("-------------------")
print(f'Total Months: {total_months}') 
print(f"Total Net Profit/Losses:  ${total_amount}") 
print(f"Average Change in Profit/Losses: ${Average:.2f}")  
print(f"Greatest Increase in Profits: {highest_profit}, ({months_PLchg[highest_profit]})")
print(f"Greatest Decrease in Profits: {lowest_profit}, ({months_PLchg[lowest_profit]})")

# write to file and print to terminal
PyBank_output = pathlib.Path("Analysis/PyBank_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=PyBank_output, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write headers
    csvwriter.writerow(['Total Months', 'Total Net P&L', 'Average Change in P&L', 'Month/Yr with Greatest Increase in Profit', 'Amount of Greatest Increase',
    'Month/Yr with Greatest Decrease in Profit', 'Amount of Greatest Decrease'])
      
    # Write results
    csvwriter.writerow([total_months, total_amount, Average, highest_profit, months_PLchg[highest_profit], lowest_profit, months_PLchg[lowest_profit]])

