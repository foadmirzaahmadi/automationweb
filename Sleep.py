from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(1)


# def wait_until_element_has_an_attribute(element_selector,element_locator,attribute,attribute_value,timeout=5,exact=True):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(element_selector,element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) == attribute_value
#             else:
#                 assert attribute_value in element.get_attribute(attribute)
#             return
#         except:
#             sleep(0.2)
#     raise Exception("element attribute is not:" + str(attribute))
#
#
# def wait_until_element_has_not_an_attribute(element_selector,element_locator,attribute,attribute_value,timeout=5,exact=True):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(element_selector,element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) != attribute_value
#             else:
#                 assert attribute_value not in element.get_attribute(attribute)
#             return
#         except:
#             sleep(0.2)
#     raise Exception("element attribute is not:"+str(attribute))
#
#
# wait_until_element_has_an_attribute(By.ID,'enabled_target','class','danger',exact=False)
# wait_until_element_has_not_an_attribute(By.ID,'enabled_target','class','success',exact=False)
# trigger.click()
# wait_until_element_has_an_attribute(By.ID,'enabled_target','class','success',exact=False)
# wait_until_element_has_not_an_attribute(By.ID,'enabled_target','class','danger',exact=False)


# def wait_unitl_element_is_enable(selector, locator, timeout):
#     for i in range(timeout * 2):
#         try:
#             element = driver.find_element(selector, locator)
#             assert element.is_enabled()
#             return
#         except:
#             sleep(0.2)
#
# driver.get('https://play1.automationcamp.ir/expected_conditions.html')
# trigger = driver.find_element(By.ID, 'enabled_trigger')
# trigger.location_once_scrolled_into_view
# trigger.click()
# wait_unitl_element_is_enable(By.ID,'enabled_target',5)
# print("element enable is now!")


def wait_unitl_element_is_visible(selector, locator, timeout):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(selector, locator)

            assert element.is_displayed()
            print("test passed")
            return
        except:
            sleep(0.5)

def wait_unitl_element_is_invisible(selector, locator, timeout):
    for i in range(timeout * 2):
        try:
            element = driver.find_element(selector, locator)

            assert not element.is_displayed()
            return
        except:
            sleep(0.5)

#visibility_target

driver.get('https://play1.automationcamp.ir/expected_conditions.html')
trigger =driver.find_element(By.ID,'visibility_trigger')
trigger.location_once_scrolled_into_view
print(driver.find_element(By.ID,"visibility_target").is_displayed())
trigger.click()
wait_unitl_element_is_visible(By.ID,"visibility_target",6)
print(driver.find_element(By.ID,"visibility_target").is_displayed())