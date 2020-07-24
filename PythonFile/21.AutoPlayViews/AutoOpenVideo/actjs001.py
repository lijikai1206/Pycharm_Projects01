# coding:utf-8

from selenium import webdriver

import time

chrome_driver = 'C:\Program Files\Python37\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver)

driver.maximize_window()

driver.implicitly_wait(8)

driver.get("https://tieba.baidu.com/index.html")

time.sleep(2)

ele = driver.find_element_by_link_text("人文自然")

driver.execute_script("arguments[0].scrollIntoView();", ele)  # 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐

# driver.execute_script("scroll(0,2400)")#大概的拖动

# driver.execute_script("arguments[0].scrollIntoView(false);",ele)#移动到元素element对象的“底端”与当前窗口的“底部”对齐

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")#移动到页面最底部