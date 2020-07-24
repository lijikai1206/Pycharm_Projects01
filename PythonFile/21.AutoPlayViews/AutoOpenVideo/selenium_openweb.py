from selenium import webdriver
import time
chrome_driver = 'D:\Program Files\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path= chrome_driver)
time.sleep(10)

#browser = webdriver.Chrome()
link = "http://tts.tmooc.cn/video/showVideo?menuId=653797&version=AIDVN201812"
browser.get(link)
content = browser.page_source
with open('source.txt') as f:
    f.write(content)
print(content)
browser.close()