from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://videojs.com/")
#通过xpath来定位元素的时候需要一层一层逐层定位
video=driver.find_element_by_xpath("/html/body/section[1]/div/video")

#返回播放文件地址
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)

#播放15s
sleep(15)

#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()",video)
