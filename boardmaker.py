# Goal:
# Read a list of entries, output 25 of them in random order as a LaTeX table.

# Imports
import random

# Constants 
ENTRIES_FILENAME = "entries.txt"
GAMES_FILENAME = "games.csv"
TABLES_FILENAME = "tables.tex"
COL_MAX = 5
BOARD_SIZE = pow(COL_MAX, 2)
GAME_LIMIT = 100

HEADER = """\\begin{center}
    {\Large Lisa \married\ Max\\\\05. August 2023}\\\\
    \\vspace{1em}
    \\textbf{\Huge Hochzeitsbingo}    
\end{center}
Ziel dieses Spiels ist es, f\\"unf aufeinander folgende Felder in horizontaler, vertikaler oder diagonaler Richtung auszuf\\"ullen. Um ein K\\"astchen ausf\\"ullen zu k\\"onnen, m\\"usst Ihr eine Person auf der Hochzeit finden, auf welche die Beschreibung des jeweiligen K\\"astchens zutrifft, und ihren Namen notieren. Mehrfachnennungen sind erlaubt.\par
Die ersten zehn Personen, die ihre Spielkarte gel\\"ost haben, d\\"urfen sich bei \emph{Jan Hoegen} einen Preis abholen.
\\vfill
"""
TABLE_BEGIN = "\\begin{tblr}{rows = 7em, columns = 6em, cells = {c, m}, hlines, vlines}"
ROW_BREAK = "\\\\ "
TABLE_END = "\\end{tblr}\\newpage \n"
SIGNATURE_LINE = "\\vspace{0.5em}\\newline\\footnotesize{\emph{Name: }\\rule{1.4cm}{0.5pt}}"

# Define Functions
def read_entries(entries_filename):
    # Return a list with all entries
    with open(entries_filename) as entries_file:
        entries = entries_file.read().split("\n") 
    return entries

def create_games(entries):
    # Return a list of all games. Every item contains a sublist with a unique gameboard.
    games = [random.sample(entries, BOARD_SIZE) for _ in range(GAME_LIMIT)]
    return games

def games_to_table(games):
    # Write a latex table for every gameboard
    i = 0 # iterate for every game
    with open(TABLES_FILENAME, "w") as latexfile:
        for sublist in games:
            latexfile.write(HEADER)
            latexfile.write(TABLE_BEGIN)
            for item in sublist:
                i += 1
                latexfile.write(f"{item}{SIGNATURE_LINE} & ")
                if i % COL_MAX == 0:     # Break the current row after every fifth item
                    latexfile.seek(latexfile.tell() - 3)    # Move back three positions to remove the last "& "
                    latexfile.write(ROW_BREAK)
            latexfile.write(TABLE_END)


entries = read_entries(ENTRIES_FILENAME)
games = create_games(entries)
games_to_table(games)
