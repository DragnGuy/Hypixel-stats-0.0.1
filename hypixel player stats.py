# Import libraries
import sys
import requests
import pandas as pd
from tabulate import tabulate

# Get the Hypixel API key and the player UUID
id = input("Please enter your player name: ")


def send_req(url):
    print("Sending request...")
    response = requests.get(url)
    print("Response:")
    data = response.json()
    return data


url = f"https://api.mojang.com/users/profiles/minecraft/{id}?"
identification = send_req(url)
if identification and "id" in identification: 
    uuid = identification["id"]
    print(uuid)
else:
    print("error please try name again")
    sys.exit()

api_key = "9e175ec6-8963-4e69-8175-98d30548ebac"

url = f"https://api.hypixel.net/v2/player?key={api_key}&uuid={uuid}"
data = send_req(url)

if data and "success" in data:
    # Your existing code for successful API response

    # player name
    if "playername" in data["player"]:
        player_name = data["player"]["playername"]
    else:
        player_name = "ACTUAL ERROR"

    # display name
    if "displayname" in ["player"]:
        display_name = data["player"]["displayname"]
    else:
        display_name = "ACTUAL ERROR"

    # Check if "newPackageRank/prefix" key exists, set default if not
    if "prefix" in data["player"]:
        rank = data["player"]["prefix"]
    elif "newPackageRank" in data["player"]:
        rank = data["player"]["newPackageRank"]
    else:
        rank = "Default"

    # Count the number of one-time achievements
    onetimeachievements_count = len(data["player"]["achievementsOneTime"]) if "achievementsOneTime" in data["player"] else 0

    # Creating the table for stats
    player_stats = pd.DataFrame({
        "Info Type": ["Player Name", "Display Name", "Rank", "one time achievements"],
        "Info": [player_name, display_name, rank, onetimeachievements_count]
    })

    # get the players bedwars games played
    total_played_bedwars_games = data["player"]["stats"]["Bedwars"]["games_played_bedwars"] if "games_played_bedwars" in data["player"]["stats"]["Bedwars"] else 0
    # get  the playes deaths in bedwars
    total_bedwars_deaths = data["player"]["stats"]["Bedwars"]["deaths_bedwars"] if "deaths_bedwars" in data["player"]["stats"]["Bedwars"] else 0
    # get final deaths
    total_final_deaths = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"] if "final_deaths_bedwars" in data["player"]["stats"]["Bedwars"] else 0
    #get the total bedwars kills
    total_bedwars_kills = data["player"]["stats"]["Bedwars"]["kills_bedwars"] if "kills_bedwars" in data["player"]["stats"]["Bedwars"] else 0
    # get the total final kills
    total_bedwars_final_kills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"] if "final_kills_bedwars" in data["player"]["stats"]["Bedwars"] else 0

    # Create a table for bedwars outside the loop
    bedwars = pd.DataFrame({
        "Info Type": ["Total Bedwars Games Played", "Total Deaths", "Total final deaths", "total kills", "Total final kills"],
        "Info": [total_played_bedwars_games, total_bedwars_deaths, total_final_deaths, total_bedwars_kills, total_bedwars_final_kills]
    })

    # Display the table stats outside the loop
    print("\nPlayer Stats:")
    print(tabulate(player_stats, headers="keys", tablefmt="fancy_grid", showindex=False))

    print("\nBedwars Stats:")
    print(tabulate(bedwars, headers="keys", tablefmt="fancy_grid", showindex=False))
else:
    print("Error in API response. Debugging information:")
    print(data)  # Print the entire response for debugging
    sys.exit()


