# Goal:
# Read a list of entries, output 25 of them in random order as a LaTeX table.

# Imports
import random

# Constants 
ENTRIESFILENAME = "entries.txt"
GAMESFILENAME = "games.csv"
TABLESFILENAME = "tables.tex"
COLMAX = 5
BOARDSIZE = pow(COLMAX, 2)
GAMELIMIT = 3

# Define Functions
def list_of_entries(entriesfilename):
    # Return a list with all entries
    entries = open(entriesfilename).read().split("\n")
    return entries

def create_games(entries):
    # Return a list of all games. Every item contains a sublist with a unique gameboard.
    games = ["0",]*GAMELIMIT
    for i in range(GAMELIMIT):
        games[i] = random.sample(entries, BOARDSIZE)
    return games

def games_to_table(games):
    # Write a latex table for every gameboard
    i = 0 # iterate for every game
    with open(TABLESFILENAME, "w") as latexfile:
        for sublist in games:
            latexfile.write(f"\\begin{{tabularx}}{{\columnwidth}}{{*{{{COLMAX}}}{{|X}}|}}\hline ")
            for item in sublist:
                i += 1
                latexfile.write(f"{item} & ")
                if i % COLMAX == 0:     # Break the current row after every fifth item
                    latexfile.seek(latexfile.tell() - 3)    # Move back three positions to remove the last "& "
                    latexfile.write("\\\\\hline ")
            latexfile.write("\\end{tabularx}\\newpage \n")


entries = list_of_entries(ENTRIESFILENAME)
create_games = create_games(entries)
games_to_table(create_games)
