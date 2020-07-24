def find_element(self, *loc):
    """
    在指定时间内，查找元素；否则抛出异常
    :param loc: 定位器
    :return: 元素 或 抛出异常
    """
    TimeOut = 20
    try:
        self.driver.implicitly_wait(TimeOut)  # 智能等待；超时设置

        element = self.driver.find_element(*loc)  # 如果element没有找到，到此处会开始等待
        if self.isDisplayTimeOut(element, TimeOut):
            self.hightlight(element)  # 高亮显示
        else:
            raise ElementNotVisibleException  # 抛出异常，给except捕获

        self.driver.implicitly_wait(0)  # 恢复超时设置
        return element

    except (NoSuchElementException, ElementNotVisibleException, UnexpectedAlertPresentException) as ex:
        self.getImage
        raise ex

def isDisplayTimeOut(self, element, timeSes):
    """
    在指定时间内，轮询元素是否显示
    :param element: 元素对象
    :param timeSes: 轮询时间
    :return: bool
    """
    start_time = int(time.time())  # 秒级时间戳
    timeStr = int(timeSes)
    while (int(time.time()) - start_time) <= timeSes:
        if element.is_displayed():
            return True
        self.wait(500)
    self.getImage
    return False