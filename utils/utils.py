from bs4 import BeautifulSoup 
import requests
import json
import os
import shutil

    

URLS = { 
    'news': "https://www.bbc.com/news",
    'nba': "https://www.balldontlie.io/#get-all-games"
}

_, columns = shutil.get_terminal_size()


def get_news():
    response = requests.get(URLS['news']) 
    soup = BeautifulSoup(response.text, 'html.parser')  
    news = soup.find_all('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor') 
    news_list = [news.get_text(strip=True) for news in news]
    # remove the navbar and footer
    for tag in soup.find_all(class_='navbar'):
        tag.decompose()
    for tag in soup.find_all(class_='footer'):
        tag.decompose()

    headlines = ''
    for news in news_list:
        news = news+'\n'
        headlines+= news.center(columns)
    return headlines

def get_nba():
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(URLS['nba'], headers=headers)
    data = json.loads(response.text)
    boundary = '_' 
    max_len = -1 
    nba = ''  
    for game in data['data']:
        info = '\n|'+str(game['home_team']['full_name'], game['home_team_score'], '-', game['visitor_team']['full_name'], game['visitor_team_score'])+ '|\n' 
        max_len = max(max_len,info.__len__())
        nba+=info
    boundary = boundary*max_len
    nba += boundary + nba + boundary
    return nba

def post_news():
    pass

def post_nba(): 
    pass

def update_news(): 
    pass
def update_nba():
    pass

def generate_json(): 
    pass