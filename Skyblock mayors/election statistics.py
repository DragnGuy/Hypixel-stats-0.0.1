# Import libraries
import requests
import pandas as pd
from tabulate import tabulate

# Get the user's Hypixel API key as input
send = input("If you want to send the request type y, if you dont want to send the request type n: ")


# Function to send a request to the specified URL and return the JSON data
def send_req(url):
    print("Sending request...")
    response = requests.get(url)
    # read response as json and then print a table using pandas
    print("Raw dump of response:")
    data = response.json()
    # print(json.dumps(data, indent=4))

    return data


# if the user want to use the command
if send == "y":
    # Construct the URL for the Hypixel API Skyblock election data
    url = f"https://api.hypixel.net/v2/resources/skyblock/election"
    # Send a request to the API and get the JSON data
    data = send_req(url)

    # Check if the API call was successful
    # If it was, create a pandas table from the json data
    if data and "success" in data:
        # Strip Mayor Data
        mayor_data = data["mayor"]
        mayor_name = mayor_data["name"]
        mayor_key = mayor_data["key"]
        mayor_perks = pd.json_normalize(mayor_data["perks"])

        # Create a pandas table from extracted mayor data above
        df_mayor = pd.DataFrame(
            {
                "Mayor Name": [mayor_name] * len(mayor_perks),
                "Mayor Key": [mayor_key] * len(mayor_perks),
                "Perk Name": mayor_perks["name"],
                "Perk Description": mayor_perks["description"],
            }
        )

        # Strip Skyblock Election Candidates Data
        candidates_data = data["mayor"]["election"]["candidates"]
        election_candidates = pd.json_normalize(candidates_data)

        # Create a pandas table from extracted Skyblock Election Candidates data
        df_candidates = pd.DataFrame(
            {
                "Candidate Name": election_candidates["name"],
                "Candidate Key": election_candidates["key"],
                "Votes": election_candidates["votes"],
                "Perk Name": election_candidates["perks"].apply(lambda x: [p["name"] for p in x]),
                "Perk Description": election_candidates["perks"].apply(lambda x: [p["description"] for p in x]),
            }
        )
       

        print("\n Mayor Details:")
        print(tabulate(df_mayor, headers="keys", tablefmt="fancy_grid", showindex=False))

        print("\n Skyblock Election Candidates:")
        print(tabulate(df_candidates, headers="keys", tablefmt="fancy_grid", showindex=False))

     

