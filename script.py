import requests
import time 
import json

def fetch_data_from_url(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the content of the response
            return response.content
        else:
            # Handle unsuccessful requests
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return None


def process():

    # Example usage
    url = "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/3/weeks/1/events"
    data = json.loads(fetch_data_from_url(url).decode())


    
    team_stats = {"JJ": [{"id": "3918298", "name": "Big Josh", "in": True, "points": 0},
    {"id": "3042519", "name": "Aaron Jones", "in": True, "points": 0},
    {"id": "4697815", "name": "Rashaad White", "in": True, "points": 0},
    {"id": "4047646", "name": "AJ Brown", "in": True, "points": 0},
    {"id": "4360939", "name": "Bateman", "in": True, "points": 0},
    {"id": "15847", "name": "T Kelce", "in": True, "points": 0},
    {"id": "15795", "name": "D Hop", "in": True, "points": 0}],
    "BNIED": [{"id": "12483", "name": "Stafford", "in": True, "points": 0},
    {"id": "4047365", "name": "J Jacobs", "in": True, "points": 0},
    {"id": "4430737", "name": "Kyrien Williams", "in": True, "points": 0},
    {"id": "4374302", "name": "Amon Ra", "in": True, "points": 0},
    {"id": "4426515", "name": "Puka Nacua", "in": True, "points": 0},
    {"id": "3116365", "name": "Mark Andrews", "in": True, "points": 0},
    {"id": "4373678", "name": "Khalil Shakir", "in": True, "points": 0}],
    "QUINN": [{"id": "4040715", "name": "J Hurts", "in": True, "points": 0},
    {"id": "3116385", "name": "Mixon", "in": True, "points": 0},
    {"id": "4241474", "name": "B Rob", "in": True, "points": 0},
    {"id": "4262921", "name": "JJetas", "in": True, "points": 0},
    {"id": "16737", "name": "Mike Evans", "in": True, "points": 0},
    {"id": "4429615", "name": "Zay Flowers", "in": True, "points": 0},
    {"id": "3121422", "name": "Scary Terry", "in": True, "points": 0}],
    "JONO": [{"id": "3916387", "name": "Lamar", "in": True, "points": 0},
    {"id": "4241985", "name": "JK", "in": True, "points": 0},
    {"id": "4038441", "name": "Justice Hill", "in": True, "points": 0},
    {"id": "4612826", "name": "Ladd Mc", "in": True, "points": 0},
    {"id": "4426388", "name": "Jameison Williams", "in": True, "points": 0},
    {"id": "3121023", "name": "Goedhert", "in": True, "points": 0},
    {"id": "4036133", "name": "TJ Hock", "in": True, "points": 0}],
    "MACK": [{"id": "3139477", "name": "Mahomes", "in": True, "points": 0},
    {"id": "4379399", "name": "Cook", "in": True, "points": 0},
    {"id": "4596448", "name": "Irving", "in": True, "points": 0},
    {"id": "4426354", "name": "GP", "in": True, "points": 0},
    {"id": "2977187", "name": "Coop", "in": True, "points": 0},
    {"id": "4430027", "name": "LaPorta", "in": True, "points": 0},
    {"id": "4258173", "name": "Collins", "in": True, "points": 0}],
    "TANNER": [{"id": "3052587", "name": "Baker", "in": True, "points": 0},
    {"id": "3929630", "name": "Saquon", "in": True, "points": 0},
    {"id": "3043078", "name": "Henry", "in": True, "points": 0},
    {"id": "4683062", "name": "Worthy", "in": True, "points": 0},
    {"id": "4429025", "name": "Johnston", "in": True, "points": 0},
    {"id": "4385690", "name": "Kincaid", "in": True, "points": 0},
    {"id": "4429205", "name": "Addison", "in": True, "points": 0}],
    "GRANT": [{"id": "3046779", "name": "Goff", "in": True, "points": 0},
    {"id": "4429795", "name": "Gibbs", "in": True, "points": 0},
    {"id": "4361529", "name": "Pacheco", "in": True, "points": 0},
    {"id": "4430834", "name": "McMillan", "in": True, "points": 0},
    {"id": "3128429", "name": "Sutton", "in": True, "points": 0},
    {"id": "4035538", "name": "Montgomery", "in": True, "points": 0},
    {"id": "4241478", "name": "DeVonta", "in": True, "points": 0}],}

    player_ids = []
    for team_name, team_players in team_stats.items():
        for player in team_players:
            player_ids.append(player['id'])

    player_points = {k: 0 for k in player_ids}

    stats = {"passingYards": .04, "passingTouchdowns": 4, "interceptions": -2, "twoPtPass": 2, "rushingYards": .1, "rushingTouchdowns": 6, "twoPtRush": 2, "receivingYards": .1, "receptions": 1, "receivingTouchdowns": 6, "twoPtReception": 2, "fumblesLost": -2}

    events = data["items"]

    for event_url in events:
        event_bytes = fetch_data_from_url(event_url['$ref'])
        event_data = json.loads(event_bytes.decode())

        competitors = event_data['competitions'][0]['competitors']
        event_id = event_data['competitions'][0]["id"]
        teams = []
        for competitor in competitors:
            teams.append(competitor['id'])

        for team_name, team_players in team_stats.items():
            for player_data in team_players:
                print(f"Processing: {player_data['name']}")
                total_points = 0
                player = player_data['id']
                for team in teams[:1]:

                    stats_url = f"http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/{event_id}/competitions/{event_id}/competitors/{team}/roster/{player}/statistics/0"
                    maybe_stat_bytes = fetch_data_from_url(stats_url)
                    if maybe_stat_bytes is None:
                        continue 
                    data = json.loads(maybe_stat_bytes.decode())

                    added = set()
                    for cat in data["splits"]["categories"]:
                        for stat in cat["stats"]:
                            name, value = stat['name'], stat['value']

                            if name in stats.keys():
                                if name in added:
                                    continue
                                added.add(name)
                                total_points += value * stats[name]
                                print(f"Adding {name}: {value} * {stats[name]}")

                    # player_points[player_id] += total_points

                    print(f"Adding {total_points}: {player_data['name']}")
                    player_data["points"] += total_points
                


    print(team_stats)


    import gspread
    gc = gspread.service_account(filename="fantasy-447619-e04c138d90f0.json")

    # Open a Google Sheet by its name
    sheet = gc.open("NFL Playoff Fantasy").sheet1  # Access the first sheet

    # Data to write (list of lists)
    sheet.clear()

    header = []
    team_names = team_stats.keys()
    for team_name in team_names:
        header += [team_name, "score"]
    # data = [[] * 10]
    # for team_name, team_players in teams.items():
    
    data = [
        header,
    ]
    sheet.update("A1", data)

    data = [[] for i in range(8)]
    print(team_stats)
    team_totals = {k: 0 for k, _ in team_stats.items()}
    for team_name, team_players in team_stats.items():
        for idx, player in enumerate(team_players):
            data[idx] += [player["name"], player["points"]]
            print(data)
            team_totals[team_name] += player["points"]
    
    sheet.update("A2", data)

    data = [[]]
    for k, v in team_totals.items():
        data[0] += ["", v]
    print(data)
    sheet.update("A9", data)


    # Clear the sheet before writing new data

    # Write the data to the sheet



while True:
    process()
    time.sleep(10)