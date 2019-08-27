import requests
import csv
import pandas

# starting off, we need to get the beer sheet from the internet
# given the league settings, get the correct beer sheet.
kickers = ['Greg Zuerlein', 'Justin Tucker', 'Harrison Butker', 'Stephen Gostokowski',
           'Wil Lutz', "Ka'imi Fairbairn", 'Mason Crosby', 'Jake Elliot', 'Brett Maher',
           'Michael Badgley', 'Robbie Gould', 'Matt Prater', 'Adam Vinatieri', 'Jason Myers',
           'Graham Gano']

defenses = ['Bears', 'Jaguars', 'Rams', 'Ravens', 'Vikings', 'Chargers', 'Texans',
                             'Browns', 'Saints', 'Broncos', 'Patriots', 'Cowboys', 'Bills', 'Eagles', 'Seahawks']

def tap(url):
    df = pandas.read_csv(url)
    df.to_csv('tap.csv')

# now we need to create a dictionary from the csv file.
def pour():
    pour = csv.DictReader(open('tap.csv'))

    players = {}
    for sip in pour:
        name = sip["Name"].title()
        del sip["Name"]
        players[name] = sip

    playersdf = pandas.DataFrame(players)
    playersdf.to_csv('players.csv')

# remove a player from the available players list
def draft(player):
    player = player.title()
    if player in kickers:
        kickers.remove(player)
    elif player in defenses:
        defenses.remove(player)
    else:
        players = pandas.read_csv('players.csv', header=0, index_col=0)
        players = players.drop(columns=player)
        players.to_csv('players.csv')

# display top 5 players available from each role
def serve():
    qbs = []
    rbs = []
    wrs = []
    tes = []
    ecr = []
    ks = []
    dst = []
    players = pandas.read_csv('players.csv', header=0, index_col=0)
    playersECR = players.T
    playersECR["ECR"] = playersECR["ECR"].astype(float)
    playersECR = playersECR.sort_values(by=["ECR"])
    playersECR = playersECR.T

    for player in players:
        if players[player]["Position"] == "QB":
            if len(qbs) < 10:
                qbs.append([player, players[player]["ECR"],
                            players[player]["ECR vs ADP"]])
        elif players[player]["Position"] == "RB":
            if len(rbs) < 10:
                rbs.append([player, players[player]["ECR"],
                            players[player]["ECR vs ADP"]])
        elif players[player]["Position"] == "WR":
            if len(wrs) < 10:
                wrs.append([player, players[player]["ECR"],
                            players[player]["ECR vs ADP"]])
        elif players[player]["Position"] == "TE":
            if len(tes) < 10:
                tes.append([player, players[player]["ECR"],
                            players[player]["ECR vs ADP"]])
        else:
            continue

    for playerECR in playersECR.keys():
        if len(ecr) < 10:
            ecr.append([playerECR, playersECR[playerECR]["ECR"],
                        playersECR[playerECR]["ECR vs ADP"]])

    for kicker in kickers:
        if len(ks) < 10:
            ks.append(kicker)

    for defense in defenses:
        if len(dst) < 10:
            dst.append(defense)

    return qbs, rbs, wrs, tes, ecr, ks, dst
