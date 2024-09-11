import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse


def check_link(url):
    try:
        response = requests.get(url)
        
        return response.status_code == 200
    except requests.RequestException:
        return False