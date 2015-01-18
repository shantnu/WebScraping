
# coding: utf-8

# In[10]:

import requests
from bs4 import BeautifulSoup
import re
import os


# In[11]:

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")
data = r.text
soup = BeautifulSoup(data)


# In[12]:

for link in soup.find_all('img'):
    print link.get("src")
    
    image = link.get("src")
    try:
        r2 = requests.get(image)

        basename, filename = os.path.split(image)

        with open(filename, "wb") as out_file:
            out_file.write(r2.content)
    except:
        pass


# In[12]:



