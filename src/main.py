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


def find_links(url):
    links = set()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for anchor in soup.find_all('a', href=True):
            link = anchor['href']
            full_url = urljoin(url, link)
            links.add(full_url)

    except requests.RequestException as e:
        print(f"Failed to retrieve the website: {e}")

    return links