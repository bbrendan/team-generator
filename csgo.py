from random import *

def teamGenerator(players):
    teamA = []
    teamB = []
    while len(players) > 0:
        playerA = choice(players)
        teamA.append(playerA)
        players.remove(playerA)
        playerB = choice(players)
        teamB.append(playerB)
        players.remove(playerB)
    fmt = "{:<10}{:<20}"
    print(fmt.format("Team A", "Team B"))
    for playerA, playerB in zip(teamA, teamB):
        print(fmt.format(playerA, playerB))

def tenManMap(maps):
    a = len(maps)
    b = randrange(0, a)
    map = maps[b]
    return map

players = ["bet", "sac", "amun", "raj", "trav", "muntake", "tanvit", "miko", "suki", "ante"]
maps = ["Mirage", "Cache", "Train", "Nuke", "Dust II", "Overpass", "Inferno", "Cobblestone", "Zoo"]

teamGenerator(players)
print("Map Selected: %s" %(tenManMap(maps)))