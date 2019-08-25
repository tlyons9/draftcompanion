import requests
import csv
import pandas

# starting off, we need to get the beer sheet from the internet
# given the league settings, get the correct beer sheet.
def tap(teams, ppr, qbs, rbs, wrs, tes, rwt, rw, wt, qrwt, pptd, pretd, prutd, pppy, ppruy, pprey, ppi, ppca, ppco, auction):
    
    url = 'https://footballabsurdity.com//wp-content/plugins/BeerSheetRequests/SHEETS/'+teams+','+ppr+','+qbs+','+rbs+','+wrs+','+tes+','+rwt+','+rw+','+wt+','+qrwt+','+pptd+','+pretd+','+prutd+','+pppy+','+ppruy+','+pprey+','+ppi+','+ppca+','+ppco+','+auction+'.csv'

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

    return players

# remove a player from the available players list
def draft(players, player):
    del players[player]
    return players

# display top 5 players available from each role
def serve(players):
    qbs = []
    rbs = []
    wrs = []
    tes = []

    for player in players:
        if players[player]["Position"] == "QB":
            if len(qbs) < 5: qbs.append(player)
        elif players[player]["Position"] == "RB":
            if len(rbs) < 5: rbs.append(player)
        elif players[player]["Position"] == "WR":
            if len(wrs) < 5: wrs.append(player)
        else:
            if len(tes) < 5: tes.append(players)

    return qbs, rbs, wrs, tes

def main():
    tap('12','0','1','2','2','1','1','0','0','0','4','6','6','0.04','0.1','0.1','-2','0','0','0')
    players = pour()

    while True:
        draft(players, player)
        qbs, rbs, wrs, tes = serve(players)
        print("QBs:")
        for q in qbs:
            print(q)
        print("RBs:")
        for r in rbs:
            print(r)
        print("WRs:")
        for w in wrs:
            print(w)
        print("TEs:")
        for t in tes:
            print(t)
        player = input("Most Recently Drafted Player: ").title()
        
if __name__ == "__main__":
    main()
