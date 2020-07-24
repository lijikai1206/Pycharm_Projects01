from socket import *
import time
import sys
import os

HOST = 'localhost'
PORT = 9500
BUFIZ = 1024
ADDR = (HOST, PORT)

def RecvFile(filename):
    print('Starting receive file....')
    f = open(filename,'wb')
    cliSockfd = socket(AF_INET, SOCK_STREAM)
    cliSockfd.send(bytes('no problem',encoding='utf-8'))
    while True:
        data = cliSockfd.recv(4096)
        if data == bytes('EOF', encoding= 'utf-8'):
            print('recved file success!')
            break
        f.write(data)
    f.close()


def SendFile(filename):
    print('starting send file...')
    cliSockfd.send(bytes('no problem',encoding='utf-8'))
    f = open(filename,'rb')
    while True:
        data = f.read(4096)
        if not data:
            time.sleep(1)
            cliSockfd.send(bytes('EOF', encoding='utf-8'))
            break
        cliSockfd.send(data)
        print('send file success!')

#处理命令方法1（接收，发送）
def handlel(act,filename):
    if act == bytes('put',encoding='utf-8'):
        print('recving msg!')
        SendFile(filename)
    elif act == bytes('get',encoding='utf-8'):
        print('sending msg!')
        SendFile(filename)
    else:
        print('error!')
#处理命令方法2（接收，发送）
def handle2(act):
    if (str(act,encoding='utf-8') == 'dir'):
        path = sys.path[0]
        every_file = os.listdir(path)
        for filename in every_file:
            cliSockfd.send(bytes(filename + '\t', encoding = 'utf-8'))
        time.sleep(1)
        eof = 'EOF'
        cliSockfd.send(bytes(eof, encoding='utf-8'))
        print('all filename has send to client success!')
    else:
        print('command error')


#服务器端运行主体
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(ADDR)
sockfd.listen(5)
while True:
    print('waiting for connection...')
    cliSockfd,addr = sockfd.accept()
    print('...connected from :',addr)

    while True:
        msg = cliSockfd.recv(4096)
        if msg == bytes('close', encoding='utf-8'):
            print('client closed')
            break
        info = msg.split()
        if len(info) ==2:
            handlel(info[0], info[1])
        elif len(info)  == 1:
            handle2(*info)
        else:
            print('command error')
            break

