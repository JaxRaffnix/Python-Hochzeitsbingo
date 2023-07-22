# Goal:
# Read a list of entries, output 25 of them in random order. Write the output in LaTeX syntax to a file.

# Imports
import random
import csv

# Set Constants 
ENTRIESFILENAME = "entries.txt"
GAMESFILENAME = "games.csv"
BOARDSIZE = 9
GAMELIMIT = 3

# Define Functions
def list_of_entries(entriesfilename):
    # Create a list that contains all the possible entries
    entries = open(entriesfilename).read().split("\n")
    return entries

def games(entries):
    # Return a list of all games. Every item contains a sublist with the gameboard.
    games = ["0",]*GAMELIMIT
    for i in range(GAMELIMIT):
        games[i] = random.sample(entries, BOARDSIZE)
    return games

def writegames(games):
    # Write each game to a row in a csv file. 
    with open(GAMESFILENAME, "w") as gamefile:
        writer = csv.writer(gamefile)
        for item in games:
            writer.writerow(item)


entries = list_of_entries(ENTRIESFILENAME)
games = games(entries)
writegames(games)

print(games)