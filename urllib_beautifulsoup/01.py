import requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")

data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
