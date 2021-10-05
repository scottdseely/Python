#Import libraries
import pathlib
import csv

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
Aberage = mean(PL_change)

#Converted list to dictionary to use in analysis


#Calc largest increase/decrease in P&L

#Summary Analysis

