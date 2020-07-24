#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
#host = "HUAWEI_P10_Plus"
print(host)
IP = socket.gethostbyname(host)
#IP = "192.168.1.102"
print(IP)
#设置端口号
port = 9100
# 连接服务，指定主机和端口
s.connect((host, port))
# 接收小于 1024 字节的数据
msg = s.recv(1024)
s.close()
print (msg.decode('utf-8'))