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
        "Info Type": ["Player Name", "Display Name", "Rank", "one time achivements"],
        "Info": [player_name, display_name, rank, onetimeachievements_count]
    })
# different types of bedwars games
    bedwars_modes = [
    "games_played_bedwars_1", "eight_one_games_played_bedwars", "games_played_bedwars", 
    "eight_two_games_played_bedwars", "four_three_games_played_bedwars", "four_four_games_played_bedwars",
    "eight_two_ultimate_games_played_bedwars", "four_four_ultimate_games_played_bedwars", 
    "castle_games_played_bedwars", "four_four_rush_games_played_bedwars", "eight_two_rush_games_played_bedwars",
    "eight_one_rush_games_played_bedwars", "eight_one_ultimate_games_played_bedwars", 
    "tourney_bedwars4s_0_games_played_bedwars", "eight_two_lucky_games_played_bedwars", 
    "four_four_lucky_games_played_bedwars", "eight_two_voidless_games_played_bedwars", 
    "four_four_voidless_games_played_bedwars", "eight_two_armed_games_played_bedwars", 
    "four_four_armed_games_played_bedwars", "two_four_games_played_bedwars", 
    "tourney_bedwars_two_four_0_games_played_bedwars", "tourney_bedwars4s_1_games_played_bedwars", 
    "eight_two_underworld_games_played_bedwars", "four_four_underworld_games_played_bedwars", 
    "four_four_swap_games_played_bedwars", "eight_two_swap_games_played_bedwars"
]

# set defalt bedwars games to 0
total_bedwars_games = 0

# Check if each bedwars mode key exists in the response and sum their values
for mode in bedwars_modes:
    if "Bedwars" in data["player"]["stats"] and mode in data["player"]["stats"]["Bedwars"]:
        total_bedwars_games += data["player"]["stats"]["Bedwars"][mode]


#bedwars deaths gamemodes
total_bedwars_death_types = [
    "deaths_bedwars", "entity_attack_deaths_bedwars", "four_four_deaths_bedwars", "four_four_entity_attack_deaths_bedwars",
    "four_four_void_deaths_bedwars", "void_deaths_bedwars", "void_deaths_bedwars", "four_four_fall_deaths_bedwars", 
    "four_four_magic_deaths_bedwars", "magic_deaths_bedwars", "entity_explosion_final_deaths_bedwars", "final_deaths_bedwars", 
    "four_four_entity_explosion_final_deaths_bedwars", "four_four_final_deaths_bedwars", "entity_attack_final_deaths_bedwars",
    "four_four_entity_attack_final_deaths_bedwars", "four_four_void_final_deaths_bedwars", "void_final_deaths_bedwars", 
    "fire_tick_deaths_bedwars", "four_four_fire_tick_deaths_bedwars", "fall_final_deaths_bedwars", "four_four_fall_final_deaths_bedwars",
    "eight_two_deaths_bedwars", "eight_two_entity_attack_deaths_bedwars", "eight_two_entity_attack_final_deaths_bedwars", 
    "eight_two_final_deaths_bedwars", "eight_two_void_deaths_bedwars", "four_four_magic_final_deaths_bedwars", 
    "magic_final_deaths_bedwars", "eight_two_void_final_deaths_bedwars", "eight_two_entity_explosion_final_deaths_bedwars",
    "eight_two_fall_final_deaths_bedwars", "four_four_projectile_deaths_bedwars", "projectile_deaths_bedwars", "four_three_deaths_bedwars",
    "four_three_entity_attack_deaths_bedwars", "four_three_entity_attack_final_deaths_bedwars", "four_three_final_deaths_bedwars",
    "four_three_void_deaths_bedwars", "four_three_entity_explosion_final_deaths_bedwars", "four_three_magic_final_deaths_bedwars",
    "eight_two_magic_deaths_bedwars", "four_three_fall_deaths_bedwars", "four_three_fall_final_deaths_bedwars", "four_three_magic_deaths_bedwars",
    "eight_two_magic_final_deaths_bedwars", "four_four_voidless_entity_attack_final_deaths_bedwars", "four_four_voidless_final_deaths_bedwars",
    "four_four_voidless_deaths_bedwars", "four_four_voidless_entity_attack_deaths_bedwars", "four_four_voidless_magic_final_deaths_bedwars", 
    "eight_two_voidless_deaths_bedwars", "eight_two_voidless_entity_attack_deaths_bedwars", "eight_two_voidless_entity_attack_final_deaths_bedwars",
    "eight_two_voidless_final_deaths_bedwars", "eight_two_fall_deaths_bedwars", "four_three_void_final_deaths_bedwars",
    "four_three_projectile_deaths_bedwars", "two_four_deaths_bedwars", "two_four_entity_attack_deaths_bedwars", "two_four_void_deaths_bedwars",
    "two_four_final_deaths_bedwars", "eight_two_fire_tick_final_deaths_bedwars", "fire_tick_final_deaths_bedwars", "eight_two_lucky_deaths_bedwars",
    "eight_two_lucky_entity_attack_final_deaths_bedwars", "eight_two_lucky_final_deaths_bedwars", "eight_two_lucky_void_deaths_bedwars",
    "eight_two_projectile_deaths_bedwars", "eight_one_deaths_bedwars", "eight_one_final_deaths_bedwars", "eight_one_void_deaths_bedwars",
    "eight_one_void_final_deaths_bedwars", "eight_one_void_final_deaths_bedwars", "eight_two_armed_entity_attack_deaths_bedwars",
    "eight_two_armed_final_deaths_bedwars", "eight_two_armed_projectile_final_deaths_bedwars", "eight_two_armed_void_deaths_bedwars",
    "two_four_fall_deaths_bedwars", "two_four_entity_attack_final_deaths_bedwars", "two_four_magic_deaths_bedwars",
    "eight_two_swap_deaths_bedwars", "eight_two_swap_deaths_bedwars", "eight_two_swap_entity_attack_final_deaths_bedwars",
    "eight_two_swap_final_deaths_bedwars", "eight_two_swap_void_deaths_bedwars", "eight_two_swap_entity_attack_deaths_bedwars",
    "eight_two_underworld_deaths_bedwars", "eight_two_underworld_entity_attack_deaths_bedwars", "eight_two_underworld_fall_final_deaths_bedwars",
    "eight_two_underworld_final_deaths_bedwars", "eight_two_underworld_void_deaths_bedwars", "eight_two_underworld_magic_final_deaths_bedwars", 
    "two_four_magic_final_deaths_bedwars", "castle_deaths_bedwars", "castle_entity_attack_deaths_bedwars", "castle_fall_deaths_bedwars",
    "castle_void_deaths_bedwars", "castle_final_deaths_bedwars", "castle_void_final_deaths_bedwars", "castle_magic_deaths_bedwars", 
    "entity_explosion_deaths_bedwars", "four_four_entity_explosion_deaths_bedwars", "four_four_fire_tick_final_deaths_bedwars",
    "two_four_fall_final_deaths_bedwars"
]
total_bedwars_deaths = 0

# Check if each bedwars death type key exists in the response and sum their values
for death_type in total_bedwars_death_types:
    if "Bedwars" in data["player"]["stats"] and death_type in data["player"]["stats"]["Bedwars"]:
        total_bedwars_deaths += data["player"]["stats"]["Bedwars"][death_type]

total_bedwars_death_types_final = [

]







# Create a table for bedwars outside the loop
bedwars = pd.DataFrame({
    "Info Type": ["Total Bedwars Games Played", "Total Deaths"],
    "Info": [total_bedwars_games, total_bedwars_deaths]
})

# Display the table stats outside the loop
print("\nPlayer Stats:")
print(tabulate(player_stats, headers="keys", tablefmt="fancy_grid", showindex=False))

print("\nBedwars Stats:")
print(tabulate(bedwars, headers="keys", tablefmt="fancy_grid", showindex=False))