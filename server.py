import socket

s = socket.socket() # two thing tcp and udp when not define bydefult tcp
print('Socket Created')

s.bind(('localhost',9999))
s.listen(3)
print('wating For connections')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", addr , name)
    c.send(bytes('Welcome to Telusko','utf-8'))
    c.close()