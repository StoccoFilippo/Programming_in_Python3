import json
from prettytable import PrettyTable

# Initialize PrettyTable
table = PrettyTable()

# Initialize lists for users and todos
users_list = []
todo_list = []

# Load todos from JSON file
with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\todos.json", "r") as todos:
    todo_list = json.load(todos)

# Load users from JSON file
with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\users.json", "r") as users:
    users_list = json.load(users)

# Iterate over each user
for user in users_list:
    # Iterate over each task
    for task in todo_list:
        # Check if the task belongs to the current user
        if task["userId"] == user["id"]:
            # Check if the task is completed and add to PrettyTable accordingly
            if task["completed"] is True:
                table.add_row(["{0}".format(task["title"]), "{0}".format("\u2705")])
            else:
                table.add_row(["{0}".format(task["title"]), "{0}".format("\u274C")])
    # Set field names for the table
    table.field_names = [user["name"], "TODO"]
    # Print the table for each user
    print(table)
