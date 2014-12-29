import requests
from bs4 import BeautifulSoup
import os
import re

# Get the page
r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")

data = r.text
soup = BeautifulSoup(data)

# Find all the image tags on the website
for link in soup.find_all('img'):
    # Print all the websites
    print(link.get("src"))

    image = link.get("src")
    try:

        # Get the image
        r2 = requests.get(image)
        base, filename = os.path.split(image)

        # Save the image to a file
        with open(filename, 'wb') as out_file:
            out_file.write(r2.content)

    except:
        # Ignore the clicky image
        pass
