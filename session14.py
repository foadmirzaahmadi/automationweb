from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
user_dir = "C:/Users/User/Desktop/projectselenium/automationweb/user_dir"
options.add_argument(f"user-data-dir={user_dir}")


driver =webdriver.Chrome(service=service,options=options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://app.clockify.me/en/signup")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("foadtest@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("foadtest123456@")
driver.find_element(By.XPATH,"//*[@class='cl-custom-control-label ng-tns-c84-3']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()