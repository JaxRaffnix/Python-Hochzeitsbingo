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

def games(entries):
    # Return a list of all games. Every item contains a sublist with the gameboard.
    games = ["0",]*GAMELIMIT
    for i in range(GAMELIMIT):
        games[i] = random.sample(entries, BOARDSIZE)
    return games

# def writegames(games):
#     # Write each game to a row in a csv file. 
#     with open(GAMESFILENAME, "w") as gamefile:
#         writer = csv.writer(gamefile)
#         for item in games:
#             writer.writerow(item)

def games_to_table(games):
    latexfile = open(LATEXFILENAME, "w")
    # with open(LATEXFILENAME, "w") as latexfile:
    latexfile.write("Test!abc")

    for sublist in games:
        latexfile.write("\\begin{tabular}{c|c|c}\hline")

        start_index = i * COLMAX
        end_index = min((i + 1) * COLMAX, len(data_list))
        sublist = games[start_index:end_index]


        sublist = sublist[:COLMAX]  # Limit the number of columns
        for item in sublist:
            latexfile.write(f"{item} & ")


entries = list_of_entries(ENTRIESFILENAME)
games = games(entries)
# writegames(games)
games_to_table(games)

print(games)