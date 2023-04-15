import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

NIKE_URLS = os.getenv("NIKE_URLS").split(",")

app = Flask(__name__)
CORS(app)


@app.route('/nike')
def scrape_nike():
    itemArray = []

    for url in NIKE_URLS:
        req = requests.get(url)
        res = req.content

        soup = BeautifulSoup(res, 'html.parser')
        names = soup.select('figure')

        for name in names:
            itemList = name.getText(" |").split(" |")
            url = name.find('a', href=True).get("href")
            brand = itemList[0]
            price = itemList[-1]
            itemArray.append({'site': "nike", 'brand': brand, 'price': price, 'url': url})

    return jsonify(itemArray)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# variabiliser le temps de la boucle par defaut 30mn

# pour faire tourner le serveur toutes les x mn et envoyer un mail, avec un while = true au debut du script, sin check sources
# if price < 60:
#     sm = smtplib.SMTP('smtp.gmail.com', 587)
#     sm.ehlo()
#     sm.starttls()
#     sm.login('mail', 'pass')
#     sm.send('mailfrom',
#             'mailto',
#             f"Subject: article trouve \n\n article trouve à {price}")
#     sm.quit()
#     time.sleep(3600) #secondes
