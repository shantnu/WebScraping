
# coding: utf-8

# In[7]:

import requests
from bs4 import BeautifulSoup
import re


# In[8]:

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")
data = r.text
soup = BeautifulSoup(data)


# In[12]:

for link in soup.find_all('p'):
    search_found = re.findall("Price: \$[\d]*", link.text)
    if search_found:
        print search_found


# In[22]:



