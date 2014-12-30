import requests
from bs4 import BeautifulSoup

# Get the page
r = requests.get("http://pythonforengineers.com/secret/")

# Get the text part of the page, and clean up the html
data = r.text
soup = BeautifulSoup(data)
print(soup.find('p').getText())
for link in soup.find_all('p'):
    try:
        print(link.getText())
    except:
        # There is some non-ascii code on the page I dont mind ignoring.
        pass