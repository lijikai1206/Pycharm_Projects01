from socket import *
import threading
from cmd import Cmd


class myclientsocket(Cmd):
    def __init__(self, host, port, BUFFSIZE):
        Cmd.__init__(self)
        self.host = host
        self.port = port
        self.buffsize = BUFFSIZE
        self.addr = (self.host, self.port)

    def conn(self):
        self.clientsocket = socket(AF_INET, SOCK_STREAM)
        # 实例名能否和类名 一样呢
        self.clientsocket.connect(self.addr)

    def rec(self):
        while 1:
            rdata = self.clientsocket.recv(self.buffsize)
            print("rec from ser: ", rdata.decode('utf8'), '\n', 'press enter to continue')

    def send(self):
        while 1:
            data = input('send>')

            self.clientsocket.send(data.encode('utf8'))


def main():
    y = myclientsocket('127.0.0.1', 21567, 1024)
    y.conn()
    t1 = threading.Thread(target=y.send, name="send")
    t2 = threading.Thread(target=y.rec, name="rec")
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
