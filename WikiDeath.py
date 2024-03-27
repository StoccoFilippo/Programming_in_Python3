import requests
import json
import wikipediaapi
from tqdm.auto import tqdm

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia("MyProjectName (merlin@example.com)", "en")

# Get the page for "Lists of deaths by year"
Lists_of_deaths_by_year = wiki_wiki.page("Lists_of_deaths_by_year")
list_years = []
url_list = []
Lists_of_deaths_by_year = Lists_of_deaths_by_year.text.split("\n")
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
deadge = {}
missing_list = []


def main():
    list_years = [x for x in range(1992, 2022)]
    create_page_url(list_years)
    scrap_wikipage(list_years, url_list)
    write_wikidead(deadge)


def create_page_url(list_years):
    """
    Create Wikipedia page URLs for each month and year.

    Parameters:
    - list_years: List of years

    Returns:
    - url_list: List of Wikipedia page URLs
    """
    for year in list_years:
        for month in months:
            url = "Deaths_in_{0}_{1}".format(month, year)
            url_list.append(url)
    return url_list


def scrap_wikipage(list_years, url_list):
    """
    Scrape Wikipedia pages for death records.

    Parameters:
    - list_years: List of years
    - url_list: List of Wikipedia page URLs

    Returns:
    - deadge: Dictionary containing death records
    """
    for year in tqdm(list_years):
        deadge[str(year)] = {}
        for month in months:
            url = "Deaths_in_{0}_{1}".format(month, year)
            deadge[str(year)][str(month)] = {}
            for day in range(1, 32):
                deadge[str(year)][str(month)][str(day)] = {}
                page_py = wiki_wiki.page(url_list[0]).section_by_title(str(day))
                death_day = page_py.text.strip("\n\n\n== References ==").split("\n")
                for record in death_day:
                    death_pp = record.split(",")
                    if len(death_pp) == 3 and death_pp is not None:
                        deadge[str(year)][str(month)][str(day)] = {
                            "Age": death_pp[1],
                            "Role": death_pp[2],
                        }
                    if len(death_pp) == 4 and death_pp is not None:
                        deadge[str(year)][str(month)][str(day)] = {
                            "Age": death_pp[1],
                            "Role": death_pp[2],
                            "cause": death_pp[3],
                        }
    return deadge


def write_wikidead(deadge):
    """
    Write death records to a JSON file.

    Parameters:
    - deadge: Dictionary containing death records
    """
    with open("c:\\Users\\Filippo\\Desktop\\Python\\Data\\Dead.json", "w") as f:
        json.dump(deadge, f, indent=3)


main()
