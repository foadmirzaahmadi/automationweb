from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options


driver =webdriver.Chrome()
driver.get("http://npanel.mojtel.ir/#/login")
# #1 ID
# el1=driver.find_element('id','searchInput')
driver.find_element('id','mat-input-0').send_keys("09359106955")
driver.find_element('id','mat-input-1').send_keys("09359106955")

sleep(9)

sleep(5)
