import pywifi
from pywifi import const

# 判断是否连接到wifi
def gic():
    wifi = pywifi.PyWiFi()      # 创建一个无线对象
    ifaces = wifi.interfaces()[0]  # 获取无线网卡
    # print(ifaces.name())
    # print(ifaces)
    print(ifaces.status())      # 打印网卡连接状态  0：未连接到wifi环境  4：连接到wifi环境
    if ifaces.status() == const.IFACE_CONNECTED:
        print('已连接')
    else:
        print('未连接！')
# 扫描附近的wifi
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()                 # 扫描wifi
    result = ifaces.scan_results()
    for name in result:
        print(name.ssid)       # ssid wifi名称


if __name__ == "__main__":
    bies()
