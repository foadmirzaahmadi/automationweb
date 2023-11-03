from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

chrome_options1 = Options()
# chrome_options1.add_argument("--incognito")
chrome_options1.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options1)
driver.get("http://yahoo.com")
sleep(3)
# driver.find_element('name','p')
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# sleep(2)
# current_path = Path(__file__).parent
# file_name=os.path.join(str(current_path),'session2.
# png')
# driver.save_screenshot(file_name)

