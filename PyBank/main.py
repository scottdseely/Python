"""
Scott Seely = Data Analytics Bootcamp

"""

#import libraries
import pathlib
import csv
import numpy as np
from termcolor import ATTRIBUTES, colored
from statistics import mean

import termcolor

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
PL_sub =  zip(profit_losses[0:], profit_losses[1:])

#List comprehension that will produce the changes in P&L for each month
PL_change = [(j-i) for i,j in PL_sub]

#Average change in P/L
Average = mean(PL_change)

#Convert list to dictionary to use in the summary
#Used months (starting at index 1) as key and the corresponding change in P/L as the value
mo_pl_change = dict(zip(months[1:], PL_change))

#Calculates greatest increase/decrease in P/L
max_profit = max(mo_pl_change.keys(), key=(lambda k: mo_pl_change[k]))
min_profit = min(mo_pl_change.keys(), key=(lambda k: mo_pl_change[k]))

#Summary to terminal
print("Financial Analysis")
print("-------------------")
print(f'Total Months: {total_months}') 
print(f"Total Net Profit/Losses:  ${total_amount}") 
termcolor.cprint(f"Average Change in Profit/Losses: ${Average:.2f}", 'red')  
print(f"Greatest Increase in Profits: {max_profit}, ({mo_pl_change[max_profit]})")
termcolor.cprint(f"Greatest Decrease in Profits: {min_profit}, ({mo_pl_change[min_profit]})", 'red')

#Summary to text
print("Financial Analysis", file=open("Analysis/Fin_AnalysisTXT.txt","a"))
print("-------------------", file=open("Analysis/Fin_AnalysisTXT.txt","a"))
print(f'Total Months: {total_months}', file=open("Analysis/Fin_AnalysisTXT.txt","a")) 
print(f"Total Net Profit/Losses:  ${total_amount}", file=open("Analysis/Fin_AnalysisTXT.txt","a")) 
termcolor.cprint(f"Average Change in Profit/Losses: ${Average:.2f}", 'red', file=open("Analysis/Fin_AnalysisTXT.txt","a"))  
print(f"Greatest Increase in Profits: {max_profit}, ({mo_pl_change[max_profit]})", file=open("Analysis/Fin_AnalysisTXT.txt","a"))
termcolor.cprint(f"Greatest Decrease in Profits: {min_profit}, ({mo_pl_change[min_profit]})", 'red', file=open("Analysis/Fin_AnalysisTXT.txt","a"))

#  Summary to csv
PyBank_output_csv = pathlib.Path("Analysis/Fin_AnalysisCSV.csv")

# Open file
with open(file=PyBank_output_csv, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write column headers 
    csvwriter.writerow(['Total Months', 'Total Net P&L', 'Average Change in P&L', 'Month/Yr with Greatest Increase in Profit', 'Amount of Greatest Increase',
    'Month/Yr with Greatest Decrease in Profit', 'Amount of Greatest Decrease'])
      
    # Write results
    csvwriter.writerow([total_months, total_amount, Average, max_profit, mo_pl_change[max_profit], min_profit, mo_pl_change[min_profit]])