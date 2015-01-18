
# coding: utf-8

# In[27]:

from selenium import webdriver


# In[28]:

driver = webdriver.Firefox()


# In[29]:

driver.get("http://pythonforengineers.com/secret/")


# In[30]:

message = driver.find_element_by_tag_name('p')


# In[31]:

print message.text


# In[32]:

buttons = driver.find_element_by_xpath("//*[(contains(text(), 'Super'))]")


# In[33]:

buttons.click()


# In[34]:

messsage = driver.find_element_by_tag_name('p')
print message.text


# In[35]:

driver.close()


# In[ ]:



