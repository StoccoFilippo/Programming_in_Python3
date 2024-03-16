import requests  # Importing requests library for making HTTP requests
import json  # Importing json library for JSON manipulation
import random  # Importing random library for random sampling

# Initialize variables
artist_list = ""
id_artist = []
block = 1
artists_info = []
artist_info = {}
artists_list_id = {}
id_artist_quest = []
answer = ""

# Insert here the artists you are interested in
to_be_searched_artists = [
    "Elio e le storie tese",
    "Queen",
    "Eminem",
    "Al Bano",
    "Mina",
    "Ghali",
    "Muse",
    "The Beatles",
    "The Rolling Stones",
    "Michael Jackson",
    "I Prevail",
    "Oasis",
    "Pink Floyd",
    "Billie Eilish",
    "Drake",
    "Peanetty",
    "Naska",
    "Daft Punk",
]

# Deezer API URLs
DEEZER_SEARCH_ARTIST_API = "https://api.deezer.com/search/artist"
DEEZER_SEARCH_ARTIST_INFO = "https://api.deezer.com/artist/"


def get_artists_ids(to_be_searched_artists):
    """
    Get the Deezer IDs for the given list of artists.

    Parameters:
    - to_be_searched_artists: List of artists to search for

    Returns:
    - artists_list_id: Dictionary containing artists and their corresponding Deezer IDs
    """
    results = {}
    for artist in to_be_searched_artists:
        r = requests.get(
            DEEZER_SEARCH_ARTIST_API, params={"q": artist, "strict": "on"}
        ).json()
        if len(r["data"]) == 0:
            print("No match found for '", artist, "'")
        elif len(r["data"]) > 1:
            print(
                "Multiple matches found for '",
                artist,
                "'. I selected the most popular match. Checkout their pic:",
                r["data"][0]["picture_big"],
            )
            artists_list_id[artist] = r["data"][0]["id"]
        else:
            print("Exactly one match found for '", artist, "'")
            artists_list_id[artist] = r["data"][0]["id"]
    json.dumps(artists_list_id)
    return artists_list_id


def select_random_id(artists_list_id):
    """
    Select random Deezer IDs from the given list of artists.

    Parameters:
    - artists_list_id: Dictionary containing artists and their corresponding Deezer IDs

    Returns:
    - id_artist_quest: List containing randomly selected Deezer IDs
    - input_artists: List containing names of artists corresponding to the selected IDs
    """
    input_artists = random.sample(list(artists_list_id.keys()), k=2)
    id_artist_quest = [int(artists_list_id[artist]) for artist in input_artists]
    return id_artist_quest, input_artists


def get_artist_info(id_artist_quest):
    """
    Get information about artists from Deezer using their IDs.

    Parameters:
    - id_artist_quest: List containing Deezer IDs of the artists to get information about

    Returns:
    - artists_info: List containing information about each artist
    """
    artists_info = []  # Initialize as an empty list
    for id in id_artist_quest:
        quest_url = "{0}{1}".format(DEEZER_SEARCH_ARTIST_INFO, id)
        artist_info = requests.get(quest_url).json()
        artists_info.append(artist_info)
    return artists_info


def quest(artists_info, block):
    """
    Quiz function to compare the number of albums between two randomly selected artists.

    Parameters:
    - artists_info: List containing information about two artists
    - block: Flag to control the execution of the quiz

    Returns:
    - block: Updated flag after completing the quiz
    """
    answer = input(
        "Which artist between {0} (1) and {1} (2) has more albums? ".format(
            artists_info[0]["name"], artists_info[1]["name"]
        )
    ).lower()
    try:
        if answer not in ["1", "2", "stop"]:
            raise ValueError
        if answer == "stop":
            block = 0
            raise NameError
        if answer == "1" and artists_info[0]["nb_album"] > artists_info[1]["nb_album"]:
            print(
                "Correct! {0} has {1} albums, while {2} has {3} albums".format(
                    artists_info[0]["name"],
                    artists_info[0]["nb_album"],
                    artists_info[1]["name"],
                    artists_info[1]["nb_album"],
                )
            )
        elif (
            answer == "2" and artists_info[0]["nb_album"] < artists_info[1]["nb_album"]
        ):
            print(
                "Correct! {0} has {1} albums, while {2} has {3} albums".format(
                    artists_info[1]["name"],
                    artists_info[1]["nb_album"],
                    artists_info[0]["name"],
                    artists_info[0]["nb_album"],
                )
            )
        else:
            print(
                "Wrong! {0} has {1} albums, while {2} has {3} albums".format(
                    artists_info[1]["name"],
                    artists_info[1]["nb_album"],
                    artists_info[0]["name"],
                    artists_info[0]["nb_album"],
                )
            )
    except ValueError:
        print("Please insert 1, 2, or 'stop' to close the program")
    except NameError:
        print("Thanks for playing")
        block = 0
    return block


def main(block):
    """
    Main function to run the quiz.

    Parameters:
    - block: Flag to control the execution of the quiz
    """
    artists_list_id = get_artists_ids(to_be_searched_artists)
    while block == 1:
        id_artist_quest, input_artists = select_random_id(artists_list_id)
        artists_info = get_artist_info(id_artist_quest)
        block = quest(artists_info, block)
        artists_info = []


main(block)
