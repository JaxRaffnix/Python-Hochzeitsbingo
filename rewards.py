REWARDSLISTFILENAME = "rewards.txt"
OUTPUTFILENAME = "output.tex"

HEADER = """\\begin{center}
    {\large Lisa \married\ Max\\\\05. August 2023}\\\\
    \\vspace{1em}
    \\textbf{\Large Sieger Hochzeitsbingo}    
\end{center}
 \n"""
text = ""

with open(REWARDSLISTFILENAME) as rewardsfile:
    rewards = rewardsfile.read().split("\n")

with open(OUTPUTFILENAME, "w") as outputfile:
    for item in rewards:
        outputfile.write(f"\hrule{HEADER}")
        outputfile.write(text)
        outputfile.write(f'Gl\\"uckwunsch! Du bist einer der ersten zehn Personen, die ihre Hochzeitsbingokarte gel\\"ost haben. Deine Belohnung ist es, das Brautpaar zu einem geeigneten Zeitpunkt \\emph{{{item}}} \\vspace{{1em}}\hrule\\newpage \n')