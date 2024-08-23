# Grab list of players from --> https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5
# Save all 5 players in player object
# Update one player age to 99 and remove one player.
# Save the update list to a file 

import requests
import json

def retrieve(url):
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.text)
    
def saveToAFile(li):
    
    with open(f"{len(li)} players.txt", "w") as file:
        file.write(json.dumps([player.to_dict() for player in li]))

class Player:
    def __init__(self, url):
        self.url = url
        self.load()

    def load(self):
        response = retrieve(self.url)
        if response:
            self.id = response["id"]
            self.fullName = response["fullName"]
            self.age = response["age"]
    
    def __repr__(self):
        return f"{self.id} {self.fullName} {self.age}"
    
    def to_dict(self):
        return {"id": self.id, "fullName": self.fullName, "age": self.age, "url": self.url}

    
url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5"

response = retrieve(url)
if response:
    players = [Player(each["$ref"]) for each in response.get("items")]
    if players:
        players[0].age = 99
        players.pop()
        saveToAFile(players)