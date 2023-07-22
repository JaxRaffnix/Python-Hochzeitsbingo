# Goal:
# Read a list of entries, output 25 of them in random order.


# Create a tuple that contains all the possible entries
entriesfilename = "entries.txt"
entries = open(entriesfilename).read().split("\n")

print(entries)