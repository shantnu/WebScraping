from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pdb

def get_code(driver):
    
    code = ""
    for code_segment in driver.find_elements_by_tag_name('pre'):
        code += code_segment.text

    with  open("code.txt", "a") as f:
        f.write("".join(code))


driver = webdriver.Firefox()
driver.get("http://pythonforengineers.com/articles/")
elem = driver.find_element_by_name("s")
elem.send_keys("reddit")
time.sleep(0.1)
elem.send_keys(Keys.RETURN)
time.sleep(0.1)
link = driver.find_element_by_link_text("Build a Reddit Bot Part 1")
link.click()

get_code(driver)

while True:
    try:
        link = driver.find_element_by_link_text("Next Part")
        link.click()
        get_code(driver)
        time.sleep(0.5)
    except:
        break

time.sleep(0.5)


driver.close()