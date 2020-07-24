import sys
import socket
import time

#环境与服务器配置
HOST = 'localhost'
PORT = 9500
BUFSIZE = 4096
ADDR = (HOST, PORT)


#接收文件方法
def RecvFile(filenaem):
    f = open(filenaem, 'wb')
    n = 0
    while True:
        msg = cliSockfd.recv(4096)
        n += 1
        if msg == bytes('EOF', encoding='utf-8'):
            print('recv file sucess!')
            break
        f.write(msg)
    f.close()
    print(n)


# 发送文件方法
def SendFile(filename):
    f = open(filename, 'rb')
    while True:
        msg = f.read()
        if not msg:
            break
        cliSockfd.sendall(msg)
    f.close()
    time.sleep(1)
    cliSockfd.sendall(bytes('EOF', encoding='utf-8'))
    print('send file success')


# 确认服务端消息方法
def confirm(cliSockfd, client_command):
    cliSockfd.send(bytes(client_command, encoding='utf-8'))
    msg = cliSockfd.recv(4096)
    if msg == bytes('no problem', encoding='utf-8'):
        return True


# 处理命令1（接收、发送）方法
def handle1(act, filename):
    if act == 'put':
        if confirm(cliSockfd, client_command):
            SendFile(filename)
        else:
            print('server error_1!')
    elif act == 'get':
        if confirm(cliSockfd, client_command):
            RecvFile(filename)
        else:
            print('server error_2!')
    else:
        print('command error!')


# 处理命令2（显示可下载文件）方法
def handle2(act):
    if act == 'dir':
        cliSockfd.send(bytes(act, encoding='utf-8'))
        while True:
            msg = cliSockfd.recv(1024)

            if msg == bytes('EOF', encoding='utf-8'):
                break
            print(msg.decode())
    else:
        print('command error')


# 客户端运行主体
# try:
cliSockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSockfd.connect(ADDR)
print('connect to', ADDR)
while True:
    client_command = input('>>>')
    if not client_command:
        continue
    msg = client_command.split()
    if len(msg) == 2:
        handle1(msg[0], msg[1])
    elif len(msg) == 1 and msg != ['close']:
        handle2(*msg)
    elif len(msg) == 1 and msg == ['close']:
        cliSockfd.send(bytes('close',encoding='utf-8'))
        break
    else:
        print('command error')
"""
except socket.error:
    print('error:',socket.error)
finally:
    cliSockfd.close()
"""
