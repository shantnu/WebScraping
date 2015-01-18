
# coding: utf-8

# In[62]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[63]:

def get_code(driver):
    '''
    Function to get the code from pre blocks, and write to a file
    '''
    
    code = ""
    
    for code_block in driver.find_elements_by_tag_name("pre"):
        code += code_block.text
    
    with open("code.txt", "a") as f:
        f.write(code)
    


# In[64]:

driver = webdriver.Firefox()


# In[65]:

driver.get("http://pythonforengineers.com/articles/")


# In[66]:

elem = driver.find_element_by_name("s")


# In[67]:

elem.send_keys("reddit")


# In[68]:

elem.send_keys(Keys.RETURN)


# In[69]:

link = driver.find_element_by_link_text("Build a Reddit Bot Part 1")


# In[70]:

link.click()


# In[71]:

get_code(driver)


# In[72]:

while True:
    try:
        link = driver.find_element_by_link_text("Next Part")
        link.click()
        get_code(driver)
    except:
        break


# In[73]:

driver.close()


# In[73]:



