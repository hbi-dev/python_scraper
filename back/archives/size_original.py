import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

SIZE_URLS = os.getenv("SIZE_URLS").split(",")

app = Flask(__name__)
CORS(app)

@app.route('/size')
def scrape_size():
    shoes = []

    for url in SIZE_URLS:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find('div', {"id": "productListRightContainer"})

        for shoe in products.findAll('li', class_='productListItem'):
            for brand in shoe.findAll('span', class_='itemTitle'):
                model = brand.text.strip()
                shoe_url = "https://www.sizeofficial.fr"+brand.find('a', href=True).get("href")
                for price in shoe.find('span', class_='pri'):
                    price = price.text.strip()
            shoes.append({
                'site': "Size?",
                'brand': model,
                'price': price,
                'url': shoe_url
            })

    return jsonify(shoes)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
