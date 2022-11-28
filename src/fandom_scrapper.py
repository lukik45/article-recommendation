
import requests
import bs4
import time
import random

def scrape_page(link):
    response = requests.get(link)
    parsed = bs4.BeautifulSoup(response.content, 'html.parser')
    





