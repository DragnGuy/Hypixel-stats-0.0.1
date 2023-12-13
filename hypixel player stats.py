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

api_key = "5ad2efd8-b2ea-4aa2-8325-84dbe3495ae6"

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
    onetimeachievements_count = len(data["player"]["achievementsOneTime"]) if "achievementsOneTime" in data["player"] else "-"

    # Creating the table for stats
    player_stats = pd.DataFrame({
        "Info Type": ["Player Name", "Display Name", "Rank", "one time achievements"],
        "Info": [player_name, display_name, rank, onetimeachievements_count]
    })

    # get the players bedwars games played
    total_played_bedwars_games = data["player"]["stats"]["Bedwars"]["games_played_bedwars"] if "games_played_bedwars" in data["player"]["stats"]["Bedwars"] else "-"
    # get  the playes deaths in bedwars
    total_bedwars_deaths = data["player"]["stats"]["Bedwars"]["deaths_bedwars"] if "deaths_bedwars" in data["player"]["stats"]["Bedwars"] else "-"
    # get final deaths
    total_final_deaths = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"] if "final_deaths_bedwars" in data["player"]["stats"]["Bedwars"] else "-"
    #get the total bedwars kills
    total_bedwars_kills = data["player"]["stats"]["Bedwars"]["kills_bedwars"] if "kills_bedwars" in data["player"]["stats"]["Bedwars"] else "-"
    # get the total final kills
    total_bedwars_final_kills = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"] if "final_kills_bedwars" in data["player"]["stats"]["Bedwars"] else "-"
    #get the total bedwars wins
    total_bedwars_wins = data["player"]["achievements"]["bedwars_wins"] if "bedwars_wins" in data["player"]["achievements"] else "-"
    #get the total losses
    total_bedwars_losses = data["player"]["stats"]["Bedwars"]["losses_bedwars"] if "losses_bedwars" in data["player"]["stats"]["Bedwars"] else "-"

    # Create a table for bedwars outside the loop
    bedwars = pd.DataFrame({
        "Info Type": ["Total Bedwars Wins", "Total Bedwars Losses", "Total Bedwars Games Played", "Total Deaths", "Total final deaths", "total kills", "Total final kills"],
        "Info": [total_bedwars_wins, total_bedwars_losses, total_played_bedwars_games, total_bedwars_deaths, total_final_deaths, total_bedwars_kills, total_bedwars_final_kills]
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


