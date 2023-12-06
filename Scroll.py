from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
acions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://www.imdb.com/chart/top/')

element = driver.find_element('link text','200. Sherlock Jr.')
print(element)
driver.execute_script("arguments[0].scrollIntoView();",element)
sleep(5)
