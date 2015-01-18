
# coding: utf-8

# In[4]:

import requests
from bs4 import BeautifulSoup


# In[5]:

r = requests.get("http://pythonforengineers.com/secret/")
data = r.text
soup = BeautifulSoup(data)


# In[9]:

for link in soup.find_all('p'):
    print link.getText()


# In[22]:



