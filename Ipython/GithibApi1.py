
# coding: utf-8

# In[19]:

import requests
import json


# In[20]:

r = requests.get("https://jobs.github.com/positions.json?description=python&location=sf")


# In[22]:

#print r.text
data = r.text

jobs_data = json.loads(data)



# In[23]:

for job in jobs_data:
    print job['title']


# In[24]:

for job in jobs_data:
    if "Django" in job['description']:
        print job['url']


# In[ ]:



