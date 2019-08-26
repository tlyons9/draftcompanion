import requests
import csv
import pandas

# starting off, we need to get the beer sheet from the internet
# given the league settings, get the correct beer sheet.
def tap(url):
    
    df = pandas.read_csv(url)
    df.to_csv('tap.csv')

# now we need to create a dictionary from the csv file.
def pour():
    pour = csv.DictReader(open('tap.csv'))

    players = {}
    for sip in pour:
        name = sip["Name"]
        del sip["Name"]
        players[name] = sip

    playersdf = pandas.DataFrame(players)
    playersdf.to_csv('players.csv')

# remove a player from the available players list
def draft(player):
    players = pandas.read_csv('players.csv',header=0,index_col=0)
    players = players.drop(columns=player)
    players.to_csv('players.csv')

# display top 5 players available from each role
def serve():
    qbs = []
    rbs = []
    wrs = []
    tes = []
    players = pandas.read_csv('players.csv',header=0,index_col=0)
    for player in players:
        if players[player]["Position"] == "QB":
            if len(qbs) < 5: qbs.append([player,players[player]["ECR"]])
        elif players[player]["Position"] == "RB":
            if len(rbs) < 5: rbs.append([player,players[player]["ECR"]])
        elif players[player]["Position"] == "WR":
            if len(wrs) < 5: wrs.append([player,players[player]["ECR"]])
        elif players[player]["Position"] == "TE":
            if len(tes) < 5: tes.append([player,players[player]["ECR"]])
        else:
            continue

    return qbs, rbs, wrs, tes
