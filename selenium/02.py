from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://pythonforengineers.com/secret")

message= driver.find_element_by_tag_name('p')

print "Before pressing the button: "
print message.text
print "\n"
button = driver.find_elements_by_xpath("//*[contains(text(), 'Super')]")

button[0].click()

print "After clicking the button: "
message= driver.find_element_by_tag_name('p')

print message.text

driver.close()