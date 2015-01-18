
# coding: utf-8

# In[17]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[18]:

driver = webdriver.Firefox()


# In[19]:

driver.get("http://pythonforengineers.com/articles/")


# In[20]:

elem = driver.find_element_by_name("s")


# In[21]:

elem.send_keys("reddit")


# In[22]:

elem.send_keys(Keys.RETURN)


# In[23]:

link = driver.find_element_by_link_text("Build a Reddit Bot Part 1")


# In[24]:

link.click()


# In[25]:

driver.close()


# In[ ]:



