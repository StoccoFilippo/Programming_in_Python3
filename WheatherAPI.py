import requests

import json

import datetime


# import the list of the different provinces
with open(
    "c:\\Users\\Filippo\\Desktop\\Python\\Data\\province.json", "r"
) as provinces_list:
    provinces = json.load(provinces_list)

print("Enter one of the following provinces")

count = 0
x = True
provinces_list2 = []
for province in provinces.items():
    count += 1
    provinces_list2.append(province[0])
    print("{0}. {1}".format(count, province[0]))

while x == True:
    state = (input("Insert the state you are interested in")).lower().capitalize()
    try:
        if state not in provinces_list2:
            raise ValueError("Provincia non presente nella lista.")

        hour = datetime.datetime.now().strftime("%H")
        date = datetime.datetime.now().strftime("%D")

        Y = datetime.datetime.now().strftime("%Y")
        M = datetime.datetime.now().strftime("%m")
        D = datetime.datetime.now().strftime("%d")

        date_ISO = "{0}-{1}-{2}".format(Y, M, D)
        date_ISO
        start_day = date_ISO
        end_day = date_ISO

        for province in provinces.items():
            if province[0] == state:
                params = {
                    "latitude": province[1]["lat"],
                    "longitude": province[1]["lon"],
                    "current": ["temperature_2m", "apparent_temperature"],
                    "hourly": ["temperature_2m", "apparent_temperature"],
                    "start_day": start_day,
                    "end_day": end_day,
                }

        url = str(
            "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&current=temperature_2m,apparent_temperature&hourly=temperature_2m,apparent_temperature&start_date={2}&end_date={3}".format(
                params["latitude"],
                params["longitude"],
                params["start_day"],
                params["end_day"],
            )
        )
        print(url)
        results = requests.get(url)

        results_json = results.json()

        counter = 0
        temperature_2m = 0
        apparent_temperature = 0
        for n in results_json["hourly"]["temperature_2m"]:
            if counter == int(hour):
                temperature_2m = n
            counter += 1
        counter = 0
        for n in results_json["hourly"]["apparent_temperature"]:
            if counter == int(hour):
                apparent_temperature = n
            counter += 1

        print(
            "The current temperature in {0} is {1} C° while the apparent temperature is {2} C°".format(
                state, temperature_2m, apparent_temperature
            )
        )
        x = False
    except:
        print("State not present in the list. Retry")
