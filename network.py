#code to open a tcp connection to a server listening on a port
#run assignment1 in server mode on port 3369 first

import socket
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('www.py4inf.com', 80))
#
# mysocket.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.1\n\n')
#
# while True:
#     data = mysocket.recv(512)
#     if len(data) < 1:
#         print 'nothing'
#         break
#     print data
# mysocket.close()

import urllib
pageHandle = urllib.urlopen('http://www.py4inf.com/code/words.txt')
for line in pageHandle:
    print line.strip()
