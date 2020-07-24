#conding:utf-8
from selenium import webdriver
import time

chrome_driver = 'C:\Program Files\Python37\chromedriver.exe'
browser = webdriver.Chrome(executable_path= chrome_driver)

browser.get("http://www.baidu.com")
time.sleep(2)
#获取页面title
title = browser.title
print(title)
#获取元素的文本
text = browser.find_element_by_id("setf").text
print(text)
#获取元素的标签
tag = browser.find_element_by_id("kw").tag_name
print(tag)
#获取元素的其他属性
name = browser.find_element_by_id("kw").get_attribute("class")
print(name)
#获取输入框的内容
browser.find_element_by_id("kw").send_keys("yoyoketang")
value = browser.find_element_by_id("kw").get_attribute("value")
print(value)
print(browser.name)