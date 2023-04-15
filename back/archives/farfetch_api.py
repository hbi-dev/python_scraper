from flask import Flask, jsonify
from flask_cors import CORS
from farfetch import Api

p = Api()
app = Flask(__name__)
CORS(app)


@app.route('/farfetch')
def scrape_farfetch():
    response = p.get_listings()
    list = []

    for item in response['listingItems']['items']:
        list.append({'site': "farfetch", 'brand': item['shortDescription'], 'price': item['priceInfo']['finalPrice'], 'url': 'https://www.farfetch.com'+item['url']})
    return jsonify(list)

if __name__ == '__main__':
    app.run(debug=True, port=5004)