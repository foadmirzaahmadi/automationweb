from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
acions = ActionChains(driver=driver)
driver.maximize_window()
driver.get('http://google.com')
driver.find_element('id','L2AGLb').click()
search_box=driver.find_element('name','q')
# search_box.send_keys("selenium" + Keys.ENTER)
# acions.key_down(Keys.CONTROL).send_keys('a').perform()
acions.key_down(Keys.SHIFT).send_keys_to_element(search_box,'selenium').key_up(Keys.SHIFT).send_keys(' selenium').perform()

search_box.click()
acions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
sleep(4)