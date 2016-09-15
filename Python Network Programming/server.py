#!/usr/bin/env python
from socket import *
sock_fd = socket(AF_INET, SOCK_STREAM)
sock_fd.bind(("192.168.0.7",9032))
sock_fd.listen(5)
while True:
    client_socket,addr = s.accept()
    print "Received Incoming Connection from ", addr
    client_socket.send("Welcom Aboard! %s\n" % a[0])
    client_socket.close()
