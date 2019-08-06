# First we'll import the os module to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Read in CSV file
csvpath = os.path.join('budget_data.csv')

# Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # for row in csvreader:
    #     print(row)

    
    mo_count = []
    tot_prof_loss = 0
    for rows in csvreader:
        # 1)Calculate number of months (rows except header)
        mo_count.append(rows[0])
        # 2) Calculate sum of Profit/Losses column
        tot_prof_loss = tot_prof_loss + int(rows[1])

    for rows in csvreader:
        # 3)Calculate average change over the data set (change from month to month)
        # Month values as list
        mo_amt = [int(rows) for i, rows in csvreader]
        print(mo_amt)
        # #something is wrong with mo_change - not getting correct output
        mo_change = [x - y for x, y in zip(mo_amt[1:], mo_amt)]
        avg_mo_change = sum(mo_change) / len(mo_change)   



    # 4)Calculate the largest increase from one month to the next (include the month)
    # 5)Calculate the largest decrease from one month to the next (include the month)

    # 6)Print results to terminal and to a text file
    print("Financial Analysis")
    print("----------------------------------------")
    print(f"Total Months: {len(mo_count)}")
    print(f"Total: ${tot_prof_loss}")
    # print(f"Average Change: ${avg_mo_change}")
    # print(f"Greatest Increase in Profits: {month value} {Profit/Loss value}")
    # print(f"Greatest Decrease in Profits: {month value} {Profit/Loss value}")
    print("----------------------------------------")


output_file = os.path.join("PyBankoutput.txt")

with open(output_file, "w", newline="") as txt:
    txt.write("Financial Analysis\n")
    txt.write("----------------------------------------\n")
    txt.write(f"Total Months: {len(mo_count)}\n")
    txt.write(f"Total: ${tot_prof_loss}\n")
    # txt.write(f"Greatest Increase in Profits: {month value} {Profit/Loss value}\n")
    # txt.write(f"Greatest Decrease in Profits: {month value} {Profit/Loss value}\n")
    print("----------------------------------------\n")