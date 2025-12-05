import requests
from bs4 import BeautifulSoup

'''
Get links from e-paper website based on a substring.

:param substr: a link will be extracted if the text contains this substring
:return: list of links
'''
def get_links(substr):
    r = requests.get('https://www.limmatwelle.ch/e-paper')
    web_output = r.text

    soup = BeautifulSoup(web_output, features='html.parser')

    links = {}
    for link in soup.find_all('a'):
        text = link.get_text()
        if substr in text:
            links[text] = link.get('href')

    return links