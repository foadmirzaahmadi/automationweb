from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)

# driver.get("https://webflow.com/made-in-webflow/website/relume-cloneable")
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//*[@class='fixed-cta migration w-inline-block']").click()
# driver.switch_to.default_content()
# driver.find_element(By.XPATH,"//span[text()='Get started']").click()
# sleep(10)


driver.get("https://play1.automationcamp.ir/frames.html")
sleep(1)
driver.switch_to.frame("frame1")
driver.find_element(By.ID, 'click_me_1').click()
sleep(1)
driver.switch_to.frame("frame2")
driver.find_element(By.ID, 'click_me_2').click()
sleep(1)
print("pass1")

driver.switch_to.parent_frame()
driver.switch_to.frame("frame3")
driver.switch_to.frame("frame4")
driver.find_element(By.ID, 'click_me_4').click()
sleep(1)
print("pass2")


def get_frame_of_element(selector, locator, _driver):
    all_frames = _driver.find_element(By.TAG_NAME, 'iframe')
    for frame in all_frames:
        _driver.switch_to.frame(frame)
        try:
            _driver.find_element(selector, locator)
            _driver.switch_to.default_content()
            return frame
        except:
            pass
    raise Exception("could not find elemet in all frames")
