import csv

movies = [["monty"],
        ["cat"],
        ["on"]]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)