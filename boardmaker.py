# Goal:
# Read a list of entries, output 25 of them in random order. Write the output in LaTeX syntax to a file.

# Imports
import random
import csv

# Set Constants 
ENTRIESFILENAME = "entries.txt"
GAMESFILENAME = "games.csv"
LATEXFILENAME = "tables.tex"
BOARDSIZE = 9
GAMELIMIT = 3
COLMAX = 3

# Define Functions
def list_of_entries(entriesfilename):
    # Create a list that contains all the possible entries
    entries = open(entriesfilename).read().split("\n")
    return entries

def create_games(entries):
    # Return a list of all games. Every item contains a sublist with a gameboard.
    games = ["0",]*GAMELIMIT
    for i in range(GAMELIMIT):
        games[i] = random.sample(entries, BOARDSIZE)
    return games

def games_to_table(games):
    # Write a latex table for every gameboard
    i = 0 # iterate for every game
    with open(LATEXFILENAME, "w") as latexfile:
        for sublist in games:
            latexfile.write("\\begin{tabular}{c|c|c}\hline ")
            for item in sublist:
                i += 1
                latexfile.write(f"{item} & ")
                if i % COLMAX == 0:     # Break row after every third item
                    latexfile.seek(latexfile.tell() - 3)  # Move back two positions to remove the last '& '
                    latexfile.write("\\\\\hline ")
            latexfile.write("\\end{tabular}\\newpage \n")


entries = list_of_entries(ENTRIESFILENAME)
create_games = create_games(entries)
games_to_table(create_games)

# print(games)