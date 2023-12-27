from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)
alert = Alert(driver)
actions = ActionChains(driver)
# driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.get('https://material.angular.io/components/snack-bar/examples')

# Get_Text_alert
# driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
# print(alert.text)


# Accept alert
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# alert.accept()
# alert_assert = driver.find_element(By.XPATH,"//*[text()='You clicked: Ok']")
# dom = driver.page_source
# assert "You clicked: Ok" in dom


# Dismiss alert
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
# alert.dismiss()
# alert_assert = driver.find_element(By.XPATH,"//*[text()='You clicked: Cancel']")
# dom = driver.page_source
# assert "You clicked: Cancel" in dom


# send text
# driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
# alert.send_keys("this is foad")
# alert.accept()
# dom =driver.page_source
# assert "this is foad" in dom


# dialog or popup

# cdk= driver.find_element(By.XPATH,"//*[@class ='mdc-button__label' and text()='CDK']")
# offset = cdk.location
# driver.find_element(By.XPATH,"//*[text()='Ok, Got it']").click()
# driver.find_element(By.XPATH,"//span[text()='Open dialog']").click()
# driver.find_element(By.XPATH,"//h3[text()='Develop across all platforms']")
# driver.find_element(By.XPATH,"//span[text()='Install']")
# driver.find_element(By.XPATH,"//span[text()='Cancel']")
# actions.move_by_offset(offset['x'],offset['y']).pause(0.5).click().perform()
# driver.find_element(By.XPATH,"//span[text()='Open dialog']").click()

#
# snack bar

input = driver.find_element(By.ID, "mat-input-4")
input.clear()
input.send_keys(1)
driver.find_element(By.XPATH,
                    "//*[@class ='mdc-button__label' and normalize-space(text())='Pizza party']//ancestor::button").click()

# 1:
driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']//*[contains(text(),'Pizza party')")

# # 2:
# driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/following::*[contains(text(),'Pizza party')")
#
# #3:
# dom =driver.page_source
# print(dom)