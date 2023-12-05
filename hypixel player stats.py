# Import libraries
import requests
import pandas as pd
from tabulate import tabulate

# Get the Hypixel API key and the player UUID
api_key = input("Please enter API key: ")
id = input("Please enter your player name: ")

def send_req(url):
    print("Sending request...")
    response = requests.get(url)
    print("Response:")
    data = response.json()
    return data

url = f"https://api.mojang.com/users/profiles/minecraft/{id}?"
identification = send_req(url)
uuid = identification["id"]
print(uuid)

url = f"https://api.hypixel.net/v2/player?key={api_key}&uuid={uuid}"
data = send_req(url)

if data and "success" in data:
    # player name
    player_name = data["player"]["playername"]

    # display name
    display_name = data["player"]["displayname"]

    # player rank/status
    if "prefix" in data["player"]:
        rank = data["player"]["prefix"]
    elif "newPackageRank" in data["player"]:
        rank = data["player"]["newPackageRank"]
    else:
        rank = "Default"

    # Creating the table
    player_stats = pd.DataFrame({
        "Info Type": ["Player Name", "Display Name", "Rank"],
        "Info": [player_name, display_name, rank]
    })

    # Display the table
    print("\nPlayer Stats:")
    print(tabulate(player_stats, headers="keys", tablefmt="fancy_grid", showindex=False))
