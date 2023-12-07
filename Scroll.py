from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
acions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(3)

# element = driver.find_element('link text','200. Sherlock Jr.')
# print(element)
# driver.execute_script("arguments[0].scrollIntoView();",element)
# sleep(5)



# def scroll_to_find_element(locator,pixel):
#     for i in range(10):
#         try:
#             driver.find_element(locator[0],locator[1])
#             return True
#         except:
#             driver.execute_script(f"window.scrollBy(0,{str(pixel)})")
#     return False
#
# driver.get('https://www.imdb.com/chart/top/')
# result = scroll_to_find_element(['link text','168. Three Billboards Outside Ebbing, Missouri'],3400)
# print(result)




# def scroll_to_find_element(locator):
#     for i in range(10):
#         try:
#             driver.find_element(locator[0],locator[1])
#             return True
#         except:
#             driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#     return False
#
# driver.get('https://www.imdb.com/chart/top/')
# result = scroll_to_find_element(['link text','rerfrfd'])
# print(result)

# page_el= driver.find_element('tag name','html')
# acions.send_keys_to_element(page_el,Keys.END).perform()
# sleep(5)

# element = driver.find_element('link text','205. Mary and Max')
# element.location_once_scrolled_into_view
# sleep(5)

# driver.get('https://material.angular.io/components/categories')
# el =driver.find_element(By.CLASS_NAME,'mdc-button__label')
# attr = el.text
# print(attr)


# el= driver.find_element(By.XPATH,"//*[@class='mdc-button__label' and text()='Components']/..")
# attr = el.get_attribute('class')
# assert  'selected' in attr, 'element is selected'
# print(attr)
# el2 = driver.find_element(By.XPATH,"//*[@class='mdc-button__label' and text()='CDK']/..").click()
# sleep(2)
# attr2 = el.get_attribute('class')
# print(attr2)
# assert  'selected' not in attr2 , 'element is not selected'
# sleep(3)

# driver.get('https://material.angular.io/components/slide-toggle/examples')
# el = driver.find_element(By.ID,'mat-radio-2')
# el3 = driver.find_element(By.ID,'mat-radio-3')
# assert 'checked' in el3.get_attribute('class')
# attr1 = el.get_attribute('class')
# assert 'checked' not in attr1
# el.click()
# attr2 = el.get_attribute('class')
# assert 'checked' in attr2
# assert 'checked' not in el3.get_attribute('class')


driver.get('https://material.angular.io/components/slide-toggle/examples')
el1 = driver.find_element(By.ID,'mat-mdc-slide-toggle-1')
assert 'checked' not in el1.get_attribute('class')
el1.click()
assert 'checked' in el1.get_attribute('class')
sleep(5)
