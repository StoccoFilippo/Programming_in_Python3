import unicodedata  # Import the unicodedata module for handling Unicode characters
import sys  # Import the sys module for interacting with the system

# Initialize variables
words = []  # List to store words entered by the user
word = ""   # String to store each word entered by the user
result = [] # List to store the Unicode code points matching the criteria
x = True    # Boolean flag to control the loop

# Function to print the Unicode table based on the words entered
def print_unicode_table(words):
    # Print the table header
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    # Initialize variables for Unicode iteration
    code = ord(" ")  # Start from the space character
    end = sys.maxunicode  # Stop at the maximum Unicode code point

    # Iterate through Unicode characters
    while code < end:
        c = chr(code)  # Get the character corresponding to the code point
        name = unicodedata.name(c, "*** unknown ***")  # Get the name of the character

        # Check if all words are present in the lowercase name of the character
        if all(word in name.lower() for word in words):
            # Print the Unicode character information
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(
                  code, name.title()))
        code += 1  # Move to the next Unicode code point

# Main loop to accept user input and print the Unicode table
while x:
    word = input("inserisci una parola: ")  # Prompt the user to input a word

    if len(word) > 1:  # Check if the input word is longer than 1 character
        if word in ("-h", "--help"):  # Check if the user asks for help
            print("usage: {0} [string]".format(sys.argv[0]))
            word = 0  # Set word to 0 to indicate no input word
        if word == "stop":  # Check if the user wants to stop the loop
            x = False  # Set x to False to exit the loop
        else:
            words.append(word.lower())  # Add the lowercase word to the list of words
else:
    print_unicode_table(words)  # Print the Unicode table based on the entered words
