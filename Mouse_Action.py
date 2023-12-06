from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
acions = ActionChains(driver=driver)
# driver.maximize_window()

# driver.find_element('id','onetrust-accept-btn-handler').click()
# driver.execute_script("scroll(0,400)")
# el = driver.find_element('xpath',"//button[text()='Double-click me']")
# acions.double_click(el).perform()
# driver.find_element('xpath',"//*[text()='Your Sample Double Click worked!']")
# sleep(3)

# el = driver.find_element('id','fname')
# acions.context_click(el).perform()
# sleep(3)

# el=driver.find_element('xpath',"//*[@class='tooltip']")
# acions.move_to_element(el).perform()
# sleep(3)

# driver.get('https://demos.telerik.com/kendo-ui/circular-gauge/index')
# driver.find_element('id','onetrust-accept-btn-handler').click()
# driver.execute_script("scroll(0,400)")
# el=driver.find_element('xpath',"//*[contains(@class,'k-button-increase')]")
# acions.click_and_hold(el).perform()
# sleep(3)

# driver.get('https://demos.telerik.com/kendo-ui/circular-gauge/index')
# sleep(3)
# driver.find_element('id',"onetrust-accept-btn-handler").click()
# driver.execute_script("scroll(0,400)")
# el = driver.find_element('xpath',"//*[contains(@class,'k-button-increase')]")
# el1 = driver.find_element('xpath',"//*[contains(@class,'k-button-decrease')]")
#
# acions.click_and_hold(el).pause(3).release().click_and_hold(el1).pause(4).perform()
# sleep(5)



# driver.get('https://selenium08.blogspot.com/2020/01/drag-drop.html')
# el1 = driver.find_element('id','draggable')
# el2 = driver.find_element('id','droppable')
#
# acions.move_to_element(el1).click_and_hold().move_to_element(el2).release().perform()
# sleep(3)

# driver.get('https://selenium08.blogspot.com/2020/01/drag-drop.html')
# el1 = driver.find_element('id','draggable')
# el2 = driver.find_element('id','droppable')
#
# acions.drag_and_drop(el1,el2).perform()
# sleep(3)

driver.get('https://trytestingthis.netlify.app/')

offset = driver.find_element('xpath',"//*[text()='Lets you select only one option']").location

driver.get('https://trytestingthis.netlify.app/')
driver.find_element('id','option').click()
acions.move_by_offset(offset['x'],offset['y']).click().perform()
sleep(4)