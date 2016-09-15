#!/usr/bin/env python
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.0.7", 9032))
s.send("Hello")
data = s.recv(10000)
print data
s.close()
