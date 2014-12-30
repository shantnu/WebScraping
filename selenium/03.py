from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://pythonforengineers.com/articles/")
elem = driver.find_element_by_name("s")
elem.send_keys("reddit")
time.sleep(0.1)
elem.send_keys(Keys.RETURN)
time.sleep(0.1)
link = driver.find_element_by_link_text("Build a Reddit Bot Part 1")
link.click()
