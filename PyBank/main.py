import os
import csv
import sys
budget_data = (os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv'))
with open(budget_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"csv Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)




