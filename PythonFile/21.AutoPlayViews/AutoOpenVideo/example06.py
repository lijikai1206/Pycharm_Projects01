#<span style="font-size:18px;">
from selenium import webdriver  #要想使用selenium 的webdriver 里的函数，首先把包导进来
import time		#调入time 函数
chrome_driver = 'C:\Program Files\Python37\chromedriver.exe'
driver = webdriver.Chrome(executable_path= chrome_driver)

#选择浏览器，可以是Firefox 、Ie 或Chrome，使用前需安装浏览器插件；
#driver是一个变量，可随便起
driver.get("http://m.mail.10086.cn")
#mplicitly_wait() 方法实现智能等待，相当于uft中的集合点，此处智能等待30秒
driver.implicitly_wait(30)
driver.find_element_by_id("ur").send_keys("15610537527")
#一个元素有若干属性id、name、（也可以用其它方式定位），此处通过id识别元素，该输入框的id叫ur ，
#我要在输入框里输入15610537527
driver.find_element_by_id("pw").send_keys("15866584957")
#网页对象操作：
#	.click()  点击对象
# .send_keys("xxx") 在对象上模拟按键输入
# .clear() 用于清除输入框的内容，比如百度输入框里默认有个“请输入关键字”的信息，
#			 再比如我们的登陆框一般默认会有“账号”“密码”这样的默认信息。
#			 clear 可以帮助我们清除这些信息。
#	.submit() 提交表单
#	.text  获取该元素的文本
#	·get_attribute("属性名，如name")   获得属性值
data1 = driver.find_element_by_class_name("loading_btn").text
print ("该元素文本为：")
print (data1)
data2 = driver.find_element_by_class_name("loading_btn").get_attribute("id")
print ("该元素id属性值为：")
print (data2)
driver.find_element_by_class_name("loading_btn").click()
#搜索的按钮的name 叫loading_btn ，我需要点一下按钮（ click() ）。
time.sleep(5)     #休眠5秒
print (driver.title) # 把页面title 打印出来
print ("：页面访问成功！")
