import os
import re

def generate_toc(directory):
    toc = "# Table des matières\n\n"

    # Liste tous les fichiers markdown dans le répertoire
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.readlines()
                toc += f"## [{filename}]({filename})\n\n"
                for line in content:
                    if line.startswith("# "):
                        toc += f"- [{line[2:].strip()}]({filename}#{line[2:].strip().replace(' ', '-')})\n"
                    elif line.startswith("## "):
                        toc += f"  - [{line[3:].strip()}]({filename}#{line[3:].strip().replace(' ', '-')})\n"
                    elif line.startswith("### "):
                        toc += f"    - [{line[4:].strip()}]({filename}#{line[4:].strip().replace(' ', '-')})\n"
                toc += "\n"

    with open(os.path.join(directory, "index.md"), 'w', encoding='utf-8') as toc_file:
        toc_file.write(toc)

    print("Table des matières générée dans TOC.md")

# Utilisation
directory = '../src/site/markdown/Day0-Introduction/"  # Répertoire actuel
generate_toc(directory)

directory = "../src/site/markdown/Day1/"  # Répertoire actuel
generate_toc(directory)

directory = "../src/site/markdown/Day2/"  # Répertoire actuel
generate_toc(directory)

directory = "../src/site/markdown/Day3-Advanced/"  # Répertoire actuel
generate_toc(directory)
