from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
alert = Alert(driver)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')



#Get_Text_alert
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# print(alert.text)


#Accept alert
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
alert.accept()
alert_assert = driver.find_element(By.XPATH,"//*[text()='You clicked Ok']")
dom = 


