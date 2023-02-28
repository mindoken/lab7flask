import requests
from bs4 import BeautifulSoup
import random
from flask import jsonify 

def get_games(count: int, shuffle:bool):
    url = "https://store.steampowered.com/search/?filter=globaltopsellers&os=win"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')


    c = 0
    items = []
    pageRequest = requests.get("https://store.steampowered.com/search/?filter=globaltopsellers&os=win")
    pageSource = BeautifulSoup(pageRequest.content,'html.parser')
    games = pageSource.find("div",attrs={"id":"search_resultsRows"}).find_all("a")
    for game in games:
        name = game.find("div", attrs={"class": "col search_name ellipsis"}).text
        date_of_publish = game.find("div", attrs={"class": "col search_released responsive_secondrow"}).text
        price = game.find("div", attrs={"class": "col search_price_discount_combined responsive_secondrow"}).text
        items.append(dict(name = name,date_of_publish = date_of_publish,price = price))
        c += 1
        if (c == count):
            break
    if (shuffle == True):
        random.shuffle(items)
    
    return items



def parse_games(name: str, date_of_publish: str, price:str):
    return jsonify(name=name,date_of_publish=date_of_publish,price=price)