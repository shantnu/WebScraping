
# coding: utf-8

# In[15]:

import requests
from bs4 import BeautifulSoup


# In[16]:

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")


# In[ ]:

for link in soup.find_all('a'):
    print link.get('href')


# In[22]:



