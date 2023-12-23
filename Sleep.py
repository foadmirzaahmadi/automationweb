from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(1)

def wait_until_element_has_an_attribute(element_selector,element_locator,attribute,attribute_value,timeout=5,exact=True):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(element_selector,element_locator)
            if exact:
                assert element.get_attribute(attribute) == attribute_value
            else:
                assert attribute_value in element.get_attribute(attribute)
            return
        except:
            sleep(0.2)
    raise Exception("element attribute is not:"+str(attribute))

driver.get('https://play1.automationcamp.ir/expected_conditions.html')
trigger= driver.find_element(By.ID,'enabled_trigger')
trigger.location_once_scrolled_into_view
trigger.click()
wait_until_element_has_an_attribute(By.ID,'enabled_target','class','success',exact=False)


