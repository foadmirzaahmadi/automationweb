from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep




driver = webdriver.Chrome()
#browser action 1 > open web
driver.get("https://google.com")
sleep(2)
driver.find_element('id','L2AGLb').click()
#
# #browser action 2 > title
# # window_title=driver.title
# # print(window_title)
# #browser action 3 > back
# # driver.get("http://wikipedia.com")
# # sleep(1)
# # driver.back()
# # sleep(1)
# #browser action 4 > forward
# # driver.forward()
#
# #browser action 5 > refresh
#
# # driver.refresh()
#
#
#
# #browser action 6 > opne new windows and switch to it(tab)
#
# # driver.switch_to.new_window('tab')
# # sleep(3)
#
# #browser action 7 > opne new windows and switch to it(windows)
# driver.switch_to.new_window('window')
# driver.get('http://yahoo.com')
# sleep(2)
# #browser action 8 > current window
#
# yahoo_window=driver.current_window_handle
# print('yahoo handle'+ str(yahoo_window))
#
#
# #browser action 9 > all handles
# all_handle=driver.window_handles
# print('all_handles'+ str(all_handle))
#
# #browser action 10 > switch
#
# driver.switch_to.window(all_handle[0])
# sleep(1)
#
#
# #browser action 11 > CLOSE TAB
#
# driver.close()
# sleep(1)
#
#
# #browser action 12 > quit TAB
#
# driver.quit()


#browser action 13 > window size


# window_size=driver.get_window_size()
# print(window_size)
# width= window_size['width']
# print(width)
# height= window_size['height']
# print(height)

#browser action 14 >set window size
# driver.set_window_size(800,600)


#browser action 15 >get widnow postition
current_position = driver.get_window_position()
print(current_position)
sleep(1)
#browser action 16 >set widnow postition

driver.set_window_position(400,500)
sleep(1)

#browser action 17 >min widnow
driver.minimize_window()
sleep(3)

#browser action 18 >max widnow

driver.maximize_window()
sleep(3)

#browser action 19 >fullscreen widnow

driver.fullscreen_window()
sleep(3)


