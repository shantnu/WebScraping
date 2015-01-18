import requests
from bs4 import BeautifulSoup
import os
import re
import pdb

# Get the page
r = requests.get("http://pythonforengineers.com")

# Get the text part of the page, and clean up the html
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('p'):
    search_term = re.findall("Price: \$([\d]*)", link.text)
    if search_term:
        print "\n Found the price: ", search_term
