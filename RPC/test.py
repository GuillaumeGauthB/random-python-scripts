import json

item = json.load(open("JSON/rochePapierCiseauxLeaderboard.json"))
for i in item['joueurs']:
    print(i)