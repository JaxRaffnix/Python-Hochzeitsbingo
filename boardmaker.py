import csv


entriesfile = csv.reader("entries.csv")
for line in entriesfile:
    entries = tuple(line)

print(entries)
