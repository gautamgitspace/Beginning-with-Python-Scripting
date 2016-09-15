#!/usr/bin/env python
from socket import *
sock_fd = socket(AF_INET, SOCK_STREAM)
sock_fd.connect(("192.168.0.7", 9032))
data = s.recv(10000)
print data
s.close()
