# Import libraries
import requests
import pandas as pd
from tabulate import tabulate

# Get the Hypixel API key and the player UUID
api_key = input("Please enter API key: ")
uuid = input("Please enter your player UUID: ")

def send_req(url):
    print("Sending request...")
    response = requests.get(url)
    print("Response:")
    data = response.json()
    return data

url = f"https://api.hypixel.net/v2/player?key={api_key}&uuid={uuid}"
data = send_req(url)

# test note
if data and "success" in data:
    player_name = data["player"]["playername"]
    display_name = data["player"]["displayname"]
    
    # Check if "newPackageRank/prefix" key exists, set default if not

if "prefix" in data["player"]:
        rank = data["player"]["prefix"]
elif "newPackageRank" in data["player"]:
        rank = data["player"]["newPackageRank"]
else:
        rank = "Default"

    # Creating the table
player_stats = pd.DataFrame({
        "Info Type:": ["Player Name", "Display Name", "Rank"],
        "Info:": [player_name, display_name, rank]
    })

    # Display the table
print("\nPlayer Stats:")
print(tabulate(player_stats, headers="keys", tablefmt="fancy_grid", showindex=True))
