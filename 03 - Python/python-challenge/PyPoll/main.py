# Import the os and csv modules
import os
import csv

# Read in CSV file
csvpath = os.path.join('election_data.csv')

# Reading using CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidate_list = []
    vote_count = 0

    for rows in csvreader:
        