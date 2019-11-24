import csv
from pathlib import Path

data_folder = Path("pyparagraph/raw_data/")

file_to_open = data_folder / "paragraph_1.txt"

with open(file_to_open, "r") as this_file:

    Text=this_file.readline
    # Cleaning text and lower casing all words
    for char in '-.,\n':
        Text=Text.replace(char,' ')
    Text = Text.lower()

