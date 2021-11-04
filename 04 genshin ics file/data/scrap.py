import requests
from bs4 import BeautifulSoup

def get_response(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def get_soup(filename=None, url=None):
    '''prioiritises file over url'''
    if filename:
        with open(filename, "r", encoding='utf-8') as f:
            html = f.read()
        f.close()
    elif url:
        response = get_response(url)
        html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def save_site_html(url, filename):
    response = get_response(url)
    with open(filename, "w", encoding='utf-8') as file:
        file.write(response.text)
    file.close()
    return filename