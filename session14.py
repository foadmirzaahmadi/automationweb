from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()

#1
# user_dir = "C:/Users/TUF/PycharmProjects/automationweb/user_dir" #user 1
# user_dir = "C:/Users/TUF/PycharmProjects/automationweb/user_dir_2" #user 2
# options.add_argument(f"user-data-dir={user_dir}")
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.get("https://app.clockify.me/en/signup")
# # driver.find_element(By.XPATH,"//input[@type='email']").send_keys("foadtest1@gmail.com")  #user 1
# driver.find_element(By.XPATH,"//input[@type='email']").send_keys("foadtest2@gmail.com")  #user 2
# driver.find_element(By.XPATH,"//input[@type='password']").send_keys("foadtest123456@")
# driver.find_element(By.XPATH,"//*[text()=' I agree to CAKE.com ']").click()
# driver.find_element(By.XPATH,"//*[text()=' Create free account ']").click()
# for i in range(10):
#     try:
#         driver.find_element(By.ID,'sidebar-menu')
#         break
#     except:
#         sleep(1)
#
# sleep(3)


# 2
# user_dir = "C:/Users/TUF/PycharmProjects/automationweb/user_dir"
user_dir = "C:/Users/TUF/PycharmProjects/automationweb/user_dir_2" #user 2

options.add_argument(f"user-data-dir={user_dir}")
driver =webdriver.Chrome(service=service,options=options)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://app.clockify.me/tracker#")

for i in range(10):
    try:
        driver.find_element(By.ID,'sidebar-menu')
        break
    except:
        sleep(1)

sleep(3)


# open without cache but keep perevious cache
# user_dir = "C:/Users/TUF/PycharmProjects/automationweb/user_dir"
# options.add_argument(f"user-data-dir={user_dir}")
# options.add_argument("--incognito")
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.get("https://app.clockify.me/tracker#")
# sleep(5)
