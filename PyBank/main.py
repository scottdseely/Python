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


#changes in P&L for each month

#Calc the avg change in P&L

#Converted list to dictionary to use in analysis


#Calc largest increase/decrease in P&L

#Summary

