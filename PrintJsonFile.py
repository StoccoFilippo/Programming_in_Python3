import json

filename = "c:\\Users\\Filippo\\Desktop\\Python\\Data\\05_email_data.json"

with open(filename, "r") as file:
    data = json.load(file)

for user in data:
    print(user["email"])
