from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options


driver =webdriver.Chrome()
driver.get("http://wikipedia.com")
# #1 ID
# el1=driver.find_element('id','searchInput')
el1=driver.find_element('css selector','#searchInput')
el1.send_keys("Hello world")
sleep(2)
#
# #2 xpath
# el2=driver.find_element('xpath',"//input[@type='search']")
# assert el1==el2
#
# el3=driver.find_element('xpath',"//*[text()='Italiano']")
# el3.click()
# sleep(3)

#3 tag
# el4=driver.find_element('tag name','select')
# el4.click()
# sleep(3)

#4 link text
# driver.find_element('link text','Download Wikipedia for Android or iOS').click()
# sleep(4)

#5 partial link text
# driver.find_element('partial link text','Download').click()
# sleep(4)

#5 class name
# driver.find_element('class name','svg-search-icon').click()
# sleep(4)

# #6 css selector
driver.find_element('css selector','.svg-search-icon').click()
sleep(4)