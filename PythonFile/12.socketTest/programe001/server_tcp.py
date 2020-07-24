# 服务器端代码++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


from socket import *
import os
from time import ctime
import threading
from cmd import Cmd


class Tcpsersocket(Cmd):
    def __init__(self):
        self.start_time = ctime()
        print('starting ', self.start_time)

    def conf(self):
        print(os.path)
        self.host = '127.0.0.1'
        self.port = 21567
        self.bufsize = 1024
        self.addr = (self.host, self.port)

        # 声明一个socket对象 tcpsersocket
        tcpsersock = socket(AF_INET, SOCK_STREAM)
        tcpsersock.bind(self.addr)
        tcpsersock.listen(5)
        quit = False
        shutdown = False
        print('waiting for connection...')

        self.clientsocket, addr = tcpsersock.accept()
        print('client connected from: ', addr)

    def send(self):
        # self.ss = ss
        while 1:
            self.ss = input("input>>")
            self.clientsocket.send(self.ss.encode('utf-8'))

    def rec(self):
        while 1:
            data = self.clientsocket.recv(self.bufsize)
            data = data.decode('utf-8')
            print('\n', ctime(), '\n', "rec from client: ", data, '\n', 'press enter to continue')


def main():
    x = Tcpsersocket()
    x.conf()
    t1 = threading.Thread(target=x.send, name="send")
    t2 = threading.Thread(target=x.rec, name="rec")
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
