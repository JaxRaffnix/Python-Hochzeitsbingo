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

HEADER = """\\begin{center}
        {\Large Lisa \married\ Max\\\\05. August 2023}\\\\
        \\vspace*{2em}
        \\textbf{\Huge Hochzeitsbingo}    
    \end{center}
    Ziel dieses Spiels ist es, f\\"unf aufeinander folgende Felder in horizontaler, vertikaler oder diagonaler Richtung abzustreichen.\par
    Um ein K\\"astchen abstreichen zu k\\"onnen, m\\"usst Ihr eine Person auf der Hochzeit finden, auf welche die Beschreibung des jeweiligen K\\"astchens passt. In dieses Feld tragt ihr dann den Namen der Person ein. Namen d\\"urfen doppelt verwendet werden.\par
    Die ersten 10 Personen, die f\\"unf K\\"astchen in einer Reihe abgestrichen haben und somit ihre Spielkarte gel\\"ost haben, d\\"urfen sich einen Preis bei \emph{Jan Hoegen} abholen.
    \\vfill
"""
TABLEBEGIN = f"\\begin{{tabularx}}{{\columnwidth}}{{*{{{COLMAX}}}{{|R}}|}}\hline "
ROWBREAK = "\\\\\hline "
TABLEEND = "\\end{tabularx}\\newpage \n"

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
            latexfile.write(HEADER)
            latexfile.write(TABLEBEGIN)
            for item in sublist:
                i += 1
                latexfile.write(f"{item} & ")
                if i % COLMAX == 0:     # Break the current row after every fifth item
                    latexfile.seek(latexfile.tell() - 3)    # Move back three positions to remove the last "& "
                    latexfile.write(ROWBREAK)
            latexfile.write(TABLEEND)


entries = list_of_entries(ENTRIESFILENAME)
games = create_games(entries)
games_to_table(games)
