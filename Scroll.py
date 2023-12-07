from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
acions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://www.imdb.com/chart/top/')

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