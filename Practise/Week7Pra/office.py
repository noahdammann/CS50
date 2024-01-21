import csv
import re

counter = 0

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().lower()
        if re.search("^(office|the.office)$", title):
            counter += 1

print(f"The number of people who enjoy The Office: {counter}") 