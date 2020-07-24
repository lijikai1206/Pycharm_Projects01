from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time

chrome_driver = 'C:\Program Files\Python37\chromedriver.exe'
browser = webdriver.Chrome(executable_path= chrome_driver)

browser.get("http://www.tmooc.cn/")
time.sleep(3)
browser.refresh()
browser.set_window_size(1200,800)
#登录TMOOC
browser.find_element_by_id('login_xxw').click()
browser.find_element_by_id('js_account_pm').clear()
browser.find_element_by_id('js_account_pm').send_keys('13600173445')
browser.find_element_by_id('js_password').clear()
browser.find_element_by_id('js_password').send_keys('ljk_3445')#password,18193445
browser.find_element_by_id('js_submit_login').click()
print("登录成功！")
time.sleep(1)
#进入我的TMOOC学习页面
browser.refresh()

ul2= "http://tts.tmooc.cn/studentCenter/toMyttsPage"
browser.get(ul2)
# a1 = browser.find_element_by_xpath("//div[@class='hide']/ul/li[9]/a").click()
# # a1 = browser.find_element_by_link_text('我的课程')i/
# print(a1)







