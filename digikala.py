from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# ایجاد یک نمونه از مرورگر Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# ایجاد یک instance از مرورگر Chrome
driver = webdriver.Chrome(options=chrome_options)

# باز کردن سایت مورد نظر
driver.get("https://www.digikala.com/search/category-power-tools/?page=6&sort=7")

# زوم مرورگر را روی 33 تنظیم می‌کنیم
driver.execute_script("document.body.style.zoom='33%'")

# پیدا کردن المان با کلاس مشخص
elements = driver.find_elements(By.CLASS_NAME, "product-list_ProductList__item__LiiNI")

# برای هر المان، کلیک کردن و باز کردن در tab جدید
for element in elements:
    # اجرای کلیک با استفاده از ActionChains
    ActionChains(driver).move_to_element(element).click().perform()

    # باز کردن tab جدید
    driver.find_element(By.css_selector('body')).send_keys(Keys.CONTROL + 't')

# بستن مرورگر
driver.quit()
