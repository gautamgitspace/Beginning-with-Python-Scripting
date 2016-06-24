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
d=dict()
m=list()
bigWord = None
bigCount = None
pageHandle = urllib.urlopen('http://www.py4inf.com/code/words.txt')
for line in pageHandle:
    line=line.strip()
    words=line.split()
    for word in words:
        d[word]=d.get(word,0)+1
        for key, value in d.items():
            #print key, value
            if bigWord is None or value > bigCount:
                bigCount=value
                bigWord=key
print bigWord, bigCount
