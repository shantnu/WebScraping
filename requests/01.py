import requests
from bs4 import BeautifulSoup

# Get the page
r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")

# Get the text part of the page, and clean up the html
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
