from flask import Flask, jsonify
from flask_cors import CORS
from nike import scrape_nike
from size import scrape_size
from farfetch import Api
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message": "Serveur up"}

@app.route('/nike')
def nike():
    items = scrape_nike()
    return jsonify(items)

@app.route('/size')
def size():
    items = scrape_size()
    return jsonify(items)

@app.route('/farfetch')
def farfetch():
    p = Api()
    response = p.get_listings()
    list = []

    named_tuple = time.localtime()  # get struct_time
    updatedtime = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    for item in response['listingItems']['items']:
        list.append({'site': "farfetch", 'brand':item['brand']['name']+' - '+ item['shortDescription'], 'price': item['priceInfo']['finalPrice'],
                     'url': 'https://www.farfetch.com' + item['url'], 'updated': updatedtime})
    return jsonify(list)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
