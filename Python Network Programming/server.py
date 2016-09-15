#!/usr/bin/env python
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.bind(("192.168.0.7",9032))
s.listen(5)
while True:
    c,a = s.accept()
    print "Received Incoming Connection from ", a
    c.send("Welcom Aboard! %s\n" % a[0])
    c.close()
