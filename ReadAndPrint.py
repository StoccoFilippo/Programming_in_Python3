# This program reads a text file and prints the fourth line.

lines = []

# Import text from file
path = "text.txt"
with open(path, "r") as text:
    # Read each line of the file
    lines = text.readlines()

# Print the fourth line
print(lines[3])
