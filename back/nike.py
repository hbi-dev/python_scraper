import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

NIKE_URLS = os.getenv("NIKE_URLS").split(",")


def scrape_nike():
    itemarray = []

    for url in NIKE_URLS:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = requests.get(url, headers=headers)
        res = req.content

        soup = BeautifulSoup(res, 'html.parser')
        names = soup.select('figure')

        for name in names:
            itemList = name.getText(" |").split(" |")
            url = name.find('a', href=True).get("href")
            brand = itemList[0]
            price = itemList[-1]
            itemarray.append({'site': "nike", 'brand': brand, 'price': price, 'url': url})

    return itemarray
