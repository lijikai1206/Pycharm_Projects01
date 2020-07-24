import socket

ip = '127.0.0.1'
port = 9100

client_socket = socket.socket() #创建socket对象
client_socket.connect((ip, port)) #创建连接
print('正在连接{}服务器,连接端口{}'.format(ip,port))

data = input(">>>>>>>>>>")
client_socket.send(data.encode())

print("连接完成")
client_socket.close()