# Open the file "users2.txt" for reading with UTF-8 encoding
filename = open("users2.txt", mode='r', encoding="utf8")

# Import the collections module
import collections

# Define constants for field indices
ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5) 

# Define a named tuple for storing user information
User = collections.namedtuple("User", "username forename middlename surname id")

# Main function to process user data and print it
def main():
    count = 0
    usernames = set() # Set to store unique usernames
    users = {} # Dictionary to store user data
    list_of_list = [] # List to store formatted user data
    for line in filename:
        line = line.rstrip() # Remove trailing spaces
        if line: 
            # Process each line of user data
            user = process_line(line, usernames)
            users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users, pagenumber)

# Function to process a line of user data
def process_line(line, usernames):
    fields = line.split(":")
    # Generate a unique username
    username = generate_username(fields, usernames)
    # Create a User namedtuple object
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user

# Function to generate a unique username
def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    # Add a number suffix if the username already exists
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

# Function to print user information in a formatted manner
def print_users(users, pagenumber):
    # List header
    current_list = [
        "{0:<{nw}} {1:^6} {2:{uw}}".format(
            "Name", "ID", "Username", nw=namewidth, uw=usernamewidth
        ),
        "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
            "", nw=namewidth, uw=usernamewidth
        )
    ]
    count = 0
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        
        if count <= pagenumber:
            name = "{0.surname}, {0.forename}{1}".format(user, initial)
            # Format user data and add to current list
            current_list.append(
                "{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(
                    name, user, nw=namewidth, uw=usernamewidth
                )
            )
            count += 1
        # Split into multiple lists if the page number is reached
        elif count > len(key):
            count = 0
            list_of_list.append(current_list)
            current_list = []
            current_list = [
                "{0:<{nw}} {1:^6} {2:{uw}}".format(
                    "Name", "ID", "Username", nw=namewidth, uw=usernamewidth
                ),
                "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
                    "", nw=namewidth, uw=usernamewidth
                )
            ]
    # Print formatted user data
    x = 0
    while x + 1 < len(list_of_list):
        if len(list_of_list[x]) == len(list_of_list[x + 1]):
            # Concatenate and print corresponding elements from two lists
            for elem1, elem2 in zip(list_of_list[x], list_of_list[x + 1]):
                risultato = elem1 + str("   ") + elem2
                print(risultato)
        else:
            print("Le liste non hanno la stessa lunghezza")
        print()
        x += 1

# Define formatting parameters
namewidth = 17
usernamewidth = 9
pagenumber = 64
list_of_list = [] # List to store formatted user data
main() # Call the main function to start execution
