from selenium import webdriver
import time

#chrome_driver = 'C:\Program Files\Python37\chromedriver.exe'
browser = webdriver.Chrome()

browser.get("http://weibo.com/")
time.sleep(3)
browser.refresh()
browser.set_window_size(2000,800)

