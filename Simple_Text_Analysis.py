# This program takes user input and analyzes the text by counting words, sentences, and some statistics about the characters used.
# It prompts the user to input words until they enter 'stop', then analyzes the text and displays statistics.

from prettytable import PrettyTable

# Initialize a PrettyTable for displaying statistics
table = PrettyTable()
table.field_names = ["Here some statistics about your text:", "#"]

# Define a list of punctuation marks
marks = [".", "!", "?", ","]

# Initialize lists and dictionaries for storing data
words = [
    "Hello",
    "!",
    "How",
    "are",
    "you",
    "doing",
    "today",
    "?",
    "I",
    "'m",
    "fine",
    ",",
    "thank",
    "you",
    ".",
]
modified_words = []
frequency = {}
max_chars = []
min_chars = []


def main(words):
    # Prompt user to input words
    ask_words(words)
    # Print the formatted text and statistics
    text, pr, word_count = print_text(words)
    stat(text, pr, word_count, frequency)


def ask_words(words):
    # Prompt user to input words until they enter 'stop'
    word = input("Insert the word: ")
    while word != "stop":
        modified_word = word.lower().strip()
        words.append(modified_word)
        print(
            "The words just introduced is: {0}\n type stop to analyze the text so far typed".format(
                modified_words
            )
        )
        word = input("Insert the word: ")
    return words


def print_text(words):
    # Print the formatted text and count words and sentences
    pr = 1
    word_count = 0
    text = ""
    new_line = True
    for word in words:
        if new_line is True:
            word.capitalize()
        if word == "stop" and word not in marks:
            word = "."
        if word not in marks:
            text = text + word + " "
            word_count += 1
        else:
            text = text.rstrip()
            text += word

        if word in marks and word != ",":
            text += "\n"
            pr += 1
            new_line = True
        if word == ",":
            text += " "
        new_line = False
    return text, pr, word_count


def stat(text, pr, word_count, frequency):
    # Calculate and print statistics about the text
    num_markers = 0
    frequency = {}
    num_words = 0
    print("\n\n Here the text correctly formatted: \n {0} ".format(text))
    for char in text.replace(" ", ""):
        if char in marks:
            num_markers += 1
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    max_char_count = max(frequency.values())
    min_char_count = min(frequency.values())

    for k, v in frequency.items():
        if v == max_char_count:
            max_chars.append(k)
        if v == min_char_count:
            min_chars.append(k)

    table.add_row(["Total number of words given: ", word_count])
    table.add_row(["Number of marks: ", num_markers])
    table.add_row(["Number of marks: ", pr])
    table.add_row(
        [
            "The most frequent ({}) character/s: ".format(max_char_count),
            ", ".join(max_chars),
        ]
    )
    table.add_row(
        [
            "The least frequent ({}) character/s: ".format(min_char_count),
            ", ".join(min_chars),
        ]
    )
    print(table)


main(words)
