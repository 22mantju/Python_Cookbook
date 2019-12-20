import csv

with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])# List of columns
    # Access individual columns with index like row[0]

