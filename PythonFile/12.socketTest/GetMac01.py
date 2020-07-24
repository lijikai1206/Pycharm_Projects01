import uuid
import psutil
from psutil import net_if_addrs
import socket
import os

#获取单个网卡
def Get_Mac():
    address = hex(uuid.getnode())[2:]
    result = '-'.join(address[i:i+2] for i in range(0,len(address),2))
    print(result)
    return result
#获取多个网卡的mac地址
def Get_More_Mac():
    for k,v in net_if_addrs().items():
        for item in v:
            address = item[1]
            if '-' in address and len(address) == 17:
                print(address)
#获取本机IP地址
def Get_Ip():
    hostname = socket.gethostname()
    print(hostname)
    hostip = socket.gethostbyname(hostname)
    print(hostip)
    return hostname,hostip
#获取ARP表
def Get_ARPList():
    os.system('arp -a > temp.txt')
    st = socket.gethostname()
    host = socket.gethostbyname(st)
    with open('temp.txt', encoding='gbk') as fp:
        for line in fp:
            line = line.split()[:2]
            if line and line[0].startswith(host[:4]) and (not line[0].endswith('255')):
                print(':'.join(line))
#获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append((k,item[1]))
    print(netcard_info)
    return netcard_info
if __name__ == "__main__":
    #Get_Mac()
    #Get_More_Mac()
    #Get_Ip()
    #Get_ARPList()
    get_netcard()