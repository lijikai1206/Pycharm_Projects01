import socket
print ("Creating socket...",)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.101', 137))
print ("done.")