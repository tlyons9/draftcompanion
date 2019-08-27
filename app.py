#from scripts.orderScript import make_order
from flask import Flask, request, url_for, redirect, render_template
import os
from tap_beer import tap, pour, serve, draft

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def grab_dict_post():
    csvurl = request.form['url']
    tap(csvurl)
    pour()
    return redirect(url_for('start_draft'))

@app.route('/draft')
def start_draft():
    qbs, rbs, wrs, tes, ecr, ks, dst = serve()
    return render_template('content.html', qbs=qbs, rbs=rbs, wrs=wrs, tes=tes, ecr=ecr, ks=ks, dst=dst)

@app.route('/draft', methods=['POST'])
def draft_player():
    player = request.form['player-name']
    draft(player)
    qbs, rbs, wrs, tes, ecr, ks, dst = serve()
    return render_template('content.html', qbs=qbs, rbs=rbs, wrs=wrs, tes=tes, ecr=ecr, ks=ks, dst=dst)

if __name__ == '__main__':
    app.run()
