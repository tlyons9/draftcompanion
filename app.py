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
    qbs, rbs, wrs, tes = serve()
    return render_template('content.html', qbs=qbs, rbs=rbs, wrs=wrs, tes=tes)

@app.route('/draft', methods=['POST'])
def draft_player():
    player = request.form['player-name']
    draft(player)
    qbs, rbs, wrs, tes = serve()
    return render_template('content.html', qbs=qbs, rbs=rbs, wrs=wrs, tes=tes)

# @app.route('/receipts/<filename>')
# def show_receipt(filename):
#     filename = 'receipts/' + filename + '.txt'
#     text = open(filename, 'r')
#     content = text.read()
#     text.close()
#     return render_template('content.html', content=content)

# @app.route('/receipts')
# def all_receipts():
#     text = os.listdir('receipts/')
#     content = text
#     return render_template('receipts.html', content=content)

# @app.route('/receipts', methods=['POST'])
# def my_receipt_post():
#     filename = request.form['filename']
#     return redirect(url_for('show_receipt', filename=filename))

# @app.route('/stash/<filename>')
# def specifc_stash(filename):
#     filename = 'stashes/' + filename + '.txt'
#     text = open(filename, 'r')
#     content = text.read()
#     text.close()
#     return render_template('content.html', content=content)

# @app.route('/orders/<filename>')
# def specifc_order(filename):
#     filename = 'orders/' + filename + '.txt'
#     text = open(filename, 'r')
#     content = text.read()
#     text.close()
#     return render_template('content.html', content=content)

# @app.route('/stash', methods=['POST'])
# def my_stash_post():
#     filename = request.form['filename']
#     return redirect(url_for('specifc_stash', filename=filename))

# @app.route('/stash')
# def all_stash():
#     text = os.listdir('stashes/')
#     content = text
#     return render_template('stash.html', content=content)

# @app.route('/orders')
# def all_orders():
#     text = os.listdir('orders/')
#     content = text
#     return render_template('orders.html', content=content)

# @app.route('/orders', methods=['POST'])
# def my_order_post():
#     filename = request.form['filename']
#     return redirect(url_for('specifc_order', filename=filename))

# @app.route('/vendor')
# def vendor():
#     text = open('vendor.txt', 'r')
#     content = text.read()
#     text.close()
#     return render_template('content.html', content=content)

if __name__ == '__main__':
    app.run()
