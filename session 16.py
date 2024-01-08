from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from time import sleep
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver.maximize_window()
driver.get("https://play2.automationcamp.ir/")
sleep(10)

driver.find_element(By.CSS_SELECTOR, "input[id='fname']").send_keys("foad tets")
sleep(4)
